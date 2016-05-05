from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader
from django.template.loader import get_template


def index(request):
    t = get_template('puzzle_view.html')
    html = t.render(Context())
    return HttpResponse(html)

def search(request):
    if 'field00' in request.GET:
        message = 'You searched for: %r' % request.GET['field00']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)