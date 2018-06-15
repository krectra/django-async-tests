import asyncio
import aiohttp

from django.views.generic import View
from django.http import HttpResponse


class IndexView(View):

    async def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world.')
