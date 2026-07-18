from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("urbano/", views.urbano, name="urbano"),
    path("intermunicipal/", views.intermunicipal, name="intermunicipal")
]

