import aiohttp

from django.views.generic import AsyncView
from django.http import HttpResponse
from django.conf import settings


class ASGIView(AsyncView):

    async def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")


async def asgi_plaintext(request):
    return HttpResponse("Hello, World!", content_type="text/plain")


async def asgi_fetch(request):
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.EXTERNAL_REQUEST_URL) as response:
            response_text = await response.text()
        return HttpResponse(response_text)
