from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Formun),
    url(r'^List/$', views.List),
    url(r'^List/Content/(?P<pk>\d+)/$', views.Content,name="Content"),
    url(r'Search/',views.Search,name="search"),
    url(r'List/Add',views.Add,name="Add")
]
