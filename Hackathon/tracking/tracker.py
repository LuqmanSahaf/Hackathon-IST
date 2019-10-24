import re
from functools import wraps

from django.http import HttpRequest, HttpResponse
from elasticsearch import Elasticsearch
from Hackathon.settings import ES_ADDRESS, ES_INDEX, ES_ENABLED
from datetime import datetime


def singleton(c):
    return c()


@singleton
class Tracker(object):
    def __init__(self):
        self.index = ES_INDEX
        self.es = Elasticsearch([ES_ADDRESS])
        self.create_index(ES_INDEX)

    def store_record(self, record):
        outcome = None
        try:
            outcome = self.es.index(index=self.index, body=record)
        except Exception as ex:
            print('Error in indexing data')
            print(str(ex))
        return outcome

    def update_record(self, record):
        pass

    def create_index(self, index=None):
        if index is None:
            index = self.index
        created = False
        # index settings
        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                "members": {
                    "properties": {
                        "url": {
                            "type": "text"
                        },
                        "from_url": {
                            "type": "text"
                        },
                        "title": {
                            "type": "text"
                        },
                        "user_id": {
                            "type": "integer"
                        },
                        "session_id": {
                            "type": "integer"
                        },
                        "timestamp": {
                            "type": "text"
                        },
                    }
                }
            }
        }

        try:
            if not self.es.indices.exists(index):
                # Ignore 400 means to ignore "Index Already Exist" error.
                self.es.indices.create(index=index, ignore=400, body=settings)
                print('Created Index')
            created = True
        except Exception as ex:
            print(str(ex))
        finally:
            return created

    def search(self, query):
        return self.es.search(index=self.index, body=query)

    @staticmethod
    def track_url(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response: HttpResponse = func(*args, **kwargs)
            if ES_ENABLED:
                request: HttpRequest = args[0]
                url = request.build_absolute_uri()
                referer = request.META.get('HTTP_REFERER')
                url = Tracker.strip_hostname(url)
                referer = Tracker.strip_hostname(referer)
                TrackedInteraction(
                    url=url,
                    from_url=referer,
                    session_id=request.session.session_key,
                    title=response.get('page_title'),
                    uid=request.user.id).save()
            response.__delitem__('page_title')
            return response
        return wrapper

    @staticmethod
    def strip_hostname(url):
        return url if url is None else '/' + url[re.compile(r'(http[s]?\:\/\/)*[a-zA-Z0-9\-\.:]*\/').search(url).end():]


class TrackedInteraction:
    def __init__(self, url=None, from_url=None, session_id=None, title=None, uid=None, tmstmp=datetime.now(),
                 interaction: dict = None):
        if interaction is None:
            self.url = url
            self.from_url = from_url
            self.session_id = session_id
            self.title = title
            self.user_id = uid
            self.timestamp = tmstmp
        else:
            self.url = interaction.get('url')
            self.from_url = interaction.get('from_url')
            self.session_id = interaction.get('session_id')
            self.title = interaction.get('title')
            self.user_id = interaction.get('user_id')
            self.timestamp = interaction.get('timestamp')

    def save(self):
        Tracker.store_record(record=self.__dict__)
