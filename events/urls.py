from django.conf.urls import patterns, url
from django.contrib import admin 
import views

urlpatterns = patterns('',
	# ex: /events/
	url(r'^$', views.list_events, name='list_events'),
)