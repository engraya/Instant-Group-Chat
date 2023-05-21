from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('', views.mainPage, name="mainPage"),
    path('registerPage', views.registerPage, name="registerPage"),
    path('loginPage', views.loginPage, name="loginPage"),
    path('logoutPage', views.logoutPage, name="logoutPage"),
    path('profilePage', views.profilePage, name="profilePage"),

]