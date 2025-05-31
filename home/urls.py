from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path('',views.home),
    path('home/',views.home),
    path('blog/',views.blog),
    path('search/',views.search),
    path('contact/',views.contact),
    path('blogpost/<str:slug>',views.blogpost),
    path('about/',views.about),
]

