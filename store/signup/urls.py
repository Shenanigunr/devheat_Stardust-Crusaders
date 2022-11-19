from django.contrib import admin
from django.urls import path, include,re_path
from signup import views

urlpatterns = [
    path('vent/', views.index, name ='home'),
    path('', views.signup, name ="signup"),
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name ="signup"),

]
