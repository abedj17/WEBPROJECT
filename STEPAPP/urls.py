from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profileVeiw, name='home'),
    path('TeacherView/', views.TeacherView, name='TeacherView'),
    path('Teachers/', views.Teachers, name='Teachers'),
    path('Students/', views.Students, name='Students'),
    path('deleteStudent/<str:id>', views.deleteStudent, name='deleteStudent'),
    path('deleteTeacher/<str:id>', views.deleteTeacher, name='deleteTeacher'),
    path('updateStudent/<str:id>', views.updateStudent, name='updateStudent'),
    path('deleteMeeting/<str:studentnumber>', views.deleteMeeting, name='deleteMeeting'),
    path('StudentView/', views.StudentView, name='StudentView'),
    path('loginView/', views.loginView, name='home-page'),
    path('meeting/', views.meeting, name='meeting'),
    path('meetingView/', views.meetingView, name='meetingView'),
    path('registerView', views.registerView, name='register'),
    path('loginView/', views.loginView, name='logout'),
    path('adminView/', views.adminView, name='adminView'),
    path('profile/', views.profile, name='profile'),
    path('adminView/', views.adminView, name='adminView'),
]