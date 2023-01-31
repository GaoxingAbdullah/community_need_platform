
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resources/", views.resources, name="resources"),
    path("request_resources/", views.requestResources, name="request_resources"),
    path("events/", views.events, name="events"),
    path("community/", views.community, name="community"),
    path("about/", views.about, name="about")
]
