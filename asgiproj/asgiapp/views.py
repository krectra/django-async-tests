import asyncio

from django.views.generic import View, TemplateView

from asgiapp.models import AsyncTest


class TestView(TemplateView):

    template_name = 'index.html'

    async def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        await asyncio.sleep(0.01)
        return self.render_to_response(context)
