from django.contrib import admin
from django.urls import path
from djangogram import views as local_views
from posts import views as posts_views


urlpatterns = [

    path("hello-world/",local_views.hello_world),
    path("sorted/", local_views.sortIntegers),
    path("hi/<str:name>/<int:age>",local_views.say_hi),
]


