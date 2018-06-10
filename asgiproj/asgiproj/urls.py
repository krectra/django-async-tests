from django.urls import path

from asgiapp.views import SleepView, FetchView


urlpatterns = [
    path('sleep/', SleepView.as_view()),
    path('fetch/', FetchView.as_view()),

]
