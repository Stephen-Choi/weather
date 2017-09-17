from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'weather'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^result/$', views.result, name='result'),
]

