from django.urls import path

from subdomains import views

urlpatterns = [
    path("", views.index, name="index"),
]
