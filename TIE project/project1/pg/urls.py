from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    path('',views.home),
    # path('',views.login),
    path('register/',views.register),
    path('dashboard.html',views.dasboard),
    path('home.html',views.home),
    path('click',views.login),
    path('login.html',views.login),
    path('register.html',views.register),
]



