from django.urls import path

from asgiapp.views import ASGIView
from wsgiapp.views import WSGIView


urlpatterns = [path("asgi/", ASGIView.as_view()), path("wsgi/", WSGIView.as_view())]
