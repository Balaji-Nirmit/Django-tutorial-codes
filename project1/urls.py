from os import name
from django.urls import path
from . import views

urlpatterns=[
  path('',views.index,name='index'),
  path('register',views.register,name='register'),
  path('login',views.login,name='login'),
  path('logout',views.logout,name='logout'),
  path('if_logged_in_only',views.if_logged_in_only,name='if_logged_in_only')
]