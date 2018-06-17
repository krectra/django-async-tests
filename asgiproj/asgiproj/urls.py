from django.urls import path

from asgiapp.views import ASGIView, asgi_plaintext, asgi_fetch
from wsgiapp.views import WSGIView, wsgi_plaintext, wsgi_fetch


urlpatterns = [
    path("asgi/", ASGIView.as_view()),
    path("asgi/fetch/", asgi_fetch),
    path("asgi/plaintext/", asgi_plaintext),
    path("wsgi/", WSGIView.as_view()),
    path("wsgi/fetch/", wsgi_fetch),
    path("wsgi/plaintext/", wsgi_plaintext),
]
