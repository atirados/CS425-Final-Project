from django.conf.urls import patterns, url
from tickets import views

urlpatterns = patterns('',
		 url(r'^$', views.theaters, name='theaters'),
		 url(r'^purchase/$', views.home, name='home'),
		 ) 

