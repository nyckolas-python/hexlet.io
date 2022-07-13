from django.urls import path

from hello_django.simple_blog.articles import views

urlpatterns = [
    path('', views.index),
]