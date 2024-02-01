from django.urls import path
from . import views

urlpatterns = [
    path('trackers', views.say_hello),
]