from django.conf.urls import patterns, url
from login import views

urlpatterns = patterns('',
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^profile/$', views.user_profile, name='profile'),
                       url(r'^update/$', views.update_profile, name='update'),
                       )