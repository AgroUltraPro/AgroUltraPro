from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.profile,name='profile'),
    path("profile",views.profile,name='profile'),
    path("notifications/",views.notification,name='notification'),
    path("prediction",views.prediction,name='prediction')
]