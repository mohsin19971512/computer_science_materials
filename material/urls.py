from django import views
from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name='profile'),
    path('questions_bank/', views.questions_bank, name='questions_bank'),
    
    path('admin_user/get_branche/<branche_id>/',views.get_branche,name='get_branche'),
    path('admin_user/get_branche_q/<branche_id>/',views.get_branche_q,name='get_branche_q'),
    
    path('admin_user/get_level/<str:id>/<str:level>/',views.get_level,name='get_level'),
    path('teaching_staff/',views.teaching_staff,name='teaching_staff'),
    #path('teacher_profile/',views.teacher_profile,name='teacher_profile'),
    path('teacher_profile/<str:id>/',views.teacher_profile,name='teacher_profile'),
    



    path('logout_user', views.logout_user, name="logout_user"),
    path('registration', views.registration, name="registration"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('doRegistration', views.doRegistration, name="doRegistration"),
    path('', views.basedashboard, name="basedashboard"),
    path('table/', views.table, name="table"),
    path('student/', views.student_form, name="student"),




]