from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('signup/', views.signup, name='signup'),
    path('input/', views.input, name='input'),
    path('bmi/', views.bmi, name='bmi'),
    path('calorie/', views.calorie, name='calorie'),
    path('logout/', views.logout_user, name="logout"),
    

    path('adminpanel/',views.adminpanel,name='adminpanel'),
    path('details/',views.detail,name='detail')
    




]
