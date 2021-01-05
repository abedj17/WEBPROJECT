from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.StudentView, name='profileStudent'),
    path('', views.loginView, name='home-page'),
    path('registerView', views.registerView, name='register'),
    path('loginView/', views.loginView, name='logout'),
    # path('profileView',views.profileView,name='profile'),
]