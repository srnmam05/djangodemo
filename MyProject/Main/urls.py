from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from crawler import views as crawlview
from Formun import views as Formunviews

urlpatterns = [
    path('', views.Index, name='Index'),
    url(r'^simple_crawl/', crawlview.simple_crawl, name='crawl'),
    url(r'^Formun/', Formunviews.Formun, name='FormunIndex'),
    url(r'^login_/',views.login_,name='login_'),
    url(r'^logout_',views.logout_,name='logout_'),
    path('signin',views.Signin,name='signin'),
    path('accounts/',include('allauth.urls')),
]
