import requests

from django.views.generic import View
from django.http import HttpResponse


class WSGIView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world.")


class WSGIFetchView(View):

    def get(self, request, *args, **kwargs):
        response = requests.get("https://now.httpbin.org/")
        return HttpResponse(response)
