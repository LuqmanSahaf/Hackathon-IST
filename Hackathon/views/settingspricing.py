from django.http import HttpResponse
from django.template import loader

from Hackathon.tracking.engine import Engine
from Hackathon.tracking.tracker import Tracker


@Engine.suggest
@Tracker.track_url
def index(request):
    template = loader.get_template('economy/settings_pricing.html')
    response = HttpResponse(template.render(request.__dict__))
    response.setdefault('page_title', template.template.nodelist[0].blocks['title'].nodelist[0].s)
    return response
