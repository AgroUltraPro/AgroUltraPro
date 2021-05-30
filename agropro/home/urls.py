from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("logout",views.logout,name='logout'),
    path("",views.index,name='home'),
    path("signup",views.signup,name='signup'),
    path("signin",views.signin,name='signin'),
    path("login",views.login,name='login'),
    
]