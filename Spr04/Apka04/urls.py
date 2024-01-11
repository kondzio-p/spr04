from django.urls import path
from . import views

urlpatterns = [
path('', views.spr04, name="spr04"),
]