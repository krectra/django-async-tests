import aiohttp

from django.views.generic import AsyncView
from django.http import HttpResponse


class ASGIView(AsyncView):

    async def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world.")


class ASGIFetchView(AsyncView):

    async def get(self, request, *args, **kwargs):
        # TODO: This doesn't get properly cleaned up atm, need to fix in the fork's ASGI handler or the HttpResponse
        async with aiohttp.ClientSession() as session:
            async with session.get("https://now.httpbin.org/") as response:
                response_text = await response.text()
        return HttpResponse(response_text)
