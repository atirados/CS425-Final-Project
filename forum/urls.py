from django.conf.urls import patterns, url
from forum import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='forum-index'),
                       url(r'^(\d+)/$', views.forum, name='forum-detail'),
                       url(r'^topic/(\d+)/$', views.topic,
                           name='topic-detail'),
                       url(r'^topic/(\d+)/less/$',
                           views.topic_less, name='topic-less'),
                       url(r'^recent/$', views.topic_recent,
                           name='topic-recent'),
                       url(r'^(\d+)/least_popular/$',
                           views.least_popular, name='least-popular'),
                       url(r'^most_comments/$', views.most_comments,
                           name='most-comments'),
                       url(r'^reply/(\d+)/$', views.post_reply, name='reply'),
                       url(r'newtopic/(\d+)/$',
                           views.new_topic, name='new-topic'),
                       )
