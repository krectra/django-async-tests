from django.urls import path

from asgiapp.views import ASGIView, ASGIFetchView
from wsgiapp.views import WSGIView, WSGIFetchView


urlpatterns = [
    path("asgi/", ASGIView.as_view()),
    path("asgi/fetch/", ASGIFetchView.as_view()),
    path("wsgi/", WSGIView.as_view()),
    path("wsgi/fetch/", WSGIFetchView.as_view()),
]
