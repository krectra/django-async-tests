from django.urls import path

from asgiapp.views import IndexView


urlpatterns = [path("test/", IndexView.as_view())]
