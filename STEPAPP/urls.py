from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('', views.loginView, name='home-page'),
    path('registerView', views.registerView, name='register')
    # path('profileView',views.profileView,name='profile'),
]