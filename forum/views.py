from django.template import RequestContext

from django.forms import models as forms_models

from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response, get_object_or_404, render

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.context_processors import csrf

from forum.models import Forum, Topic, Post
from forum.forms import TopicForm, PostForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from login.models import UserProfile

from settings import *

import sys

from django.db.models import Count

GOLD_THRESHOLD = 500
PLATINUM_THRESHOLD = 1000


def index(request):
    """Main listing."""
    forums = Forum.objects.all()
    return render_to_response("forum/list.html", {'forums': forums,
                                                  'user': request.user},
                              context_instance=RequestContext(request))


def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d


def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items


def forum(request, forum_id):
    """Listing of topics in a forum."""
    topics = Topic.objects.filter(forum=forum_id).order_by("-created")
    topics = mk_paginator(request, topics, DJANGO_SIMPLE_FORUM_TOPICS_PER_PAGE)

    forum = get_object_or_404(Forum, pk=forum_id)

    return render_to_response("forum/forum.html", add_csrf(request, topics=topics, pk=forum_id, forum=forum),
                              context_instance=RequestContext(request))


def least_popular(request, forum_id):
    topics = Topic.objects.filter(forum=forum_id).annotate(
        num_replies=Count('post')).order_by("num_replies")[0]
    # topics = mk_paginator(request, topics, DJANGO_SIMPLE_FORUM_TOPICS_PER_PAGE)

    # forum = get_object_or_404(Forum, pk=forum_id)

    # return render_to_response("forum/least_popular.html", add_csrf(request, topics=topics, pk=forum_id, forum=forum),
    #                           context_instance=RequestContext(request))
    context_dict = {'topics': topics}
    return render(request, "forum/least_popular.html", context_dict)
    # return render_to_response("forum/least_popular.html", {'topics': topics,
    #                                              'user': request.user},
    #                          context_instance=RequestContext(request))


def most_comments(request):
    users = User.objects.annotate(
        num_comments=Count('post')).order_by("-num_comments")[0]
    context_dict = {'users': users}
    return render(request, "forum/most_comments.html", context_dict)


def topic(request, topic_id):
    """Listing of posts in a topic."""
    posts = Post.objects.filter(topic=topic_id).order_by("created")
    posts = mk_paginator(request, posts, DJANGO_SIMPLE_FORUM_REPLIES_PER_PAGE)
    topic = Topic.objects.get(pk=topic_id)
    return render_to_response("forum/topic.html", add_csrf(request, posts=posts, pk=topic_id,
                                                           topic=topic), context_instance=RequestContext(request))


def topic_less(request, topic_id):
    """Listing of posts in a topic."""
    posts = Post.objects.filter(topic=topic_id).order_by("-created")[:3]
    posts = mk_paginator(request, posts, DJANGO_SIMPLE_FORUM_REPLIES_PER_PAGE)
    topic = Topic.objects.get(pk=topic_id)
    return render_to_response("forum/topic_less.html", add_csrf(request, posts=posts, pk=topic_id,
                                                                topic=topic), context_instance=RequestContext(request))


def topic_recent(request):
    """Listing of posts in a topic."""
    posts = Post.objects.all().order_by("-created")[:3]
    posts = mk_paginator(request, posts, DJANGO_SIMPLE_FORUM_REPLIES_PER_PAGE)
    # topic = Topic.objects.get(pk=topic_id)
    return render_to_response("forum/topic_recent.html", add_csrf(request, posts=posts), context_instance=RequestContext(request))


@login_required
def post_reply(request, topic_id):
    form = PostForm()
    topic = Topic.objects.get(pk=topic_id)

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():

            post = Post()
            post.topic = topic
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']

            post.creator = request.user

            userToUpdate = UserProfile.objects.get(user=request.user)

            nCredits = userToUpdate.credits
            userToUpdate.credits = int(float(nCredits + 100))

            # TODO: Change status (if points+100>threshold -> status changes) Alert???
            # Alert? Maybe return to page with status update info for user.
            # Make Gold/Platinum distinction

            if nCredits + 100 >= GOLD_THRESHOLD:
                newStatus = "Gold"
                userToUpdate.status = newStatus
                userToUpdate.save()
                post.user_ip = request.META['REMOTE_ADDR']
                post.save()
                return render_to_response("forum/status_change.html", {'status':  newStatus}, context_instance=RequestContext(request))
            elif nCredits + 100 >= PLATINUM_THRESHOLD:
                newStatus = "Platinum"
                userToUpdate.status = newStatus
                userToUpdate.save()
                post.user_ip = request.META['REMOTE_ADDR']
                post.save()
                return render_to_response("forum/status_change.html", {'status':  newStatus}, context_instance=RequestContext(request))
            else:
                userToUpdate.save()
                post.user_ip = request.META['REMOTE_ADDR']
                post.save()
                return HttpResponseRedirect(reverse('topic-detail', args=(topic.id, )))

    return render_to_response('forum/reply.html', {
        'form': form,
        'topic': topic,
    }, context_instance=RequestContext(request))


@login_required
def new_topic(request, forum_id):
    form = TopicForm()
    forum = get_object_or_404(Forum, pk=forum_id)

    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():

            topic = Topic()
            topic.title = form.cleaned_data['title']
            topic.description = form.cleaned_data['description']
            topic.forum = forum
            topic.creator = request.user
            userToUpdate = UserProfile.objects.get(user=request.user)
            nCredits = userToUpdate.credits
            userToUpdate.credits = int(float(nCredits + 200))

            # TODO: Change status (if points+100>threshold -> status changes)
            # Alert? Maybe return to page with status update info for user.
            # Make Gold/Platinum distinction

            if nCredits + 200 >= GOLD_THRESHOLD:
                newStatus = "Gold"
                userToUpdate.status = newStatus
                userToUpdate.save()
                topic.save()
                return render_to_response("forum/status_change.html", {'status':  newStatus}, context_instance=RequestContext(request))
            elif nCredits + 100 >= PLATINUM_THRESHOLD:
                newStatus = "Platinum"
                userToUpdate.status = newStatus
                userToUpdate.save()
                topic.save()
                return render_to_response("forum/status_change.html", {'status':  newStatus}, context_instance=RequestContext(request))
            else:
                userToUpdate.save()
                topic.save()
                return HttpResponseRedirect(reverse('forum-detail', args=(forum_id, )))

    return render_to_response('forum/new-topic.html', {
        'form': form,
        'forum': forum,
    }, context_instance=RequestContext(request))
