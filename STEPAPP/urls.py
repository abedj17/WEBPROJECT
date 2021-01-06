from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profileVeiw, name='home'),
    path('TeacherView/', views.TeacherView, name='TeacherView'),
    path('StudentView/', views.StudentView, name='StudentView'),
    path('loginView/', views.loginView, name='home-page'),
    path('registerView', views.registerView, name='register'),
    path('loginView/', views.loginView, name='logout'),
    path('StudentView/', views.StudentView, name='StudentView'),
    # path('profileView',views.profileView,name='profile'),
]