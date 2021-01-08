from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profileVeiw, name='home'),
    path('TeacherView/', views.TeacherView, name='TeacherView'),
    path('Teachers/', views.Teachers, name='Teachers'),
    path('deleteStudent/<str:id>', views.deleteStudent, name='deleteStudent'),
    path('deleteTeacher/<str:id>', views.deleteTeacher, name='deleteTeacher'),
    path('updateStudent/<str:id>', views.updateStudent, name='updateStudent'),
    path('StudentView/', views.StudentView, name='StudentView'),
    path('loginView/', views.loginView, name='home-page'),
    path('registerView', views.registerView, name='register'),
    path('loginView/', views.loginView, name='logout'),
    path('adminView/', views.adminView, name='adminView')
]