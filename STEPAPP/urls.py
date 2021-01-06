from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profileVeiw, name='home'),
    path('TeacherView/', views.TeacherView, name='TeacherView'),
    path('Teachers/', views.Teachers, name='Teachers'),
    #path('deleteStudent/', views.deleteStudent, name='deleteStudent'),
    path('StudentView/', views.StudentView, name='StudentView'),
    path('loginView/', views.loginView, name='home-page'),
    path('registerView', views.registerView, name='register'),
    #path('TeacherView/', views.StudentView, name='TeacherView'),
    path('loginView/', views.loginView, name='logout'),
    path('adminView/', views.adminView, name='adminView')
]