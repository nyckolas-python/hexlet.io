from django.urls import path

from hello_django.simple_blog.categories import views

urlpatterns = [
    path('', views.index),
]