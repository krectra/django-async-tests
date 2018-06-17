import requests

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings


class WSGIView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")


def wsgi_plaintext(request):
    return HttpResponse("Hello, World!", content_type="text/plain")


def wsgi_fetch(request):
    response = requests.get(settings.EXTERNAL_REQUEST_URL)
    return HttpResponse(response)
