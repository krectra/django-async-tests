from django.views.generic import AsyncView
from django.http import HttpResponse


class ASGIView(AsyncView):

    async def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world.')
