from django.views.generic import View
from django.http import HttpResponse


class WSGIView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world.')
