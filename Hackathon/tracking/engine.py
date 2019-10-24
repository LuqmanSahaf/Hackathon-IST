# from functools import wraps
from functools import wraps

from django.http import HttpRequest

from Hackathon.settings import ES_ENABLED
from .tracker import Tracker, TrackedInteraction


class Engine:
    def __init__(self):
        pass

    @staticmethod
    def find_suggestions(url):
        query = {
            "query": {
                "term": {"from_url.keyword": url}
            },
            "sort": [{"timestamp": "desc"}],
            "from": 0, "size": 3,
        }
        res = Tracker.search(query=query)
        interaction = TrackedInteraction(interaction=res['hits']['hits'][0]['_source'])
        return Suggestion(interaction.url, interaction.title)

    @staticmethod
    def suggest(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if ES_ENABLED:
                request: HttpRequest = args[0]
                url = Tracker.strip_hostname(request.build_absolute_uri())
                suggestion = Engine.find_suggestions(url)
                request.__setattr__('suggestion', suggestion)
            return func(*args, **kwargs)
        return wrapper


class Suggestion:
    def __init__(self, url, title):
        self.url = url
        self. title = title
