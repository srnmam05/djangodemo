from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
path('',views.simple_crawl),
path('POST_crawl/',views.POST_crawl),
]