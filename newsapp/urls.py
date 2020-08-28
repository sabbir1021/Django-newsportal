from django.contrib import admin
from django.urls import path,re_path

from .import views
urlpatterns = [
    path('', views.index, name="home"),
    path('post/<int:id>', views.singel, name="single"),
    path('topic/<int:id>', views.topic, name="category"),
    path('create', views.create , name="post"),
]
