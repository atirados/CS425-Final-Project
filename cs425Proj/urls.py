from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'cs425Proj.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^movies/', include('movies.urls')),
                       url(r'^', include('home.urls')),
                       url(r'^login/', include('login.urls')),
                       url(r'^forum/', include('forum.urls')),
                       url(r'^tickets/', include('tickets.urls')),
                       # url(r'^queries/', include('queries.urls')),
                       )
