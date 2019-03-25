from django.urls import path, include
from django.contrib import admin

from . import views
# app_name='blogs'

urlpatterns = [
    path('', views.BlogView.as_view(), name='index'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user special/',views.HomeView,name='home'),
    path('',views.BlogView.as_view(),name='blog_index'),
    path('profile/<slug:username>/',views.Profile,name='profile'),


    path('read/<int:pk>/',views.FullBlogView.as_view(),name='full-blog'),

    #ajax urls
    
]
