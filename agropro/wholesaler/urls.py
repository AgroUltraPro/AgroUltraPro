from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.profile,name='profile'),
    path("profile",views.profile,name='profile'),
    path("farmersmarket/",views.market,name='market'),
    path("notifications/",views.notification,name='notification'),
    path("editProfile",views.editProfile,name='editProfile'),
]