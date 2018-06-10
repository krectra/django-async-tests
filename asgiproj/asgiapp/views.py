import asyncio
import aiohttp

from django.views.generic import View, TemplateView

from asgiapp.models import FetchData


class SleepView(TemplateView):

    template_name = 'index.html'

    async def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        await asyncio.sleep(0.01)
        return self.render_to_response(context)


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.text()
            fetch_data = FetchData.objects.create(data=response)


class FetchView(TemplateView):

    template_name = 'index.html'

    async def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        loop = asyncio.get_event_loop()
        loop.create_task(fetch('https://status.github.com/api/status.json'))
        fetch_data = FetchData.objects.last()
        context['fetch_data'] = fetch_data
        return self.render_to_response(context)
