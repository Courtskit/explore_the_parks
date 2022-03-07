from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]