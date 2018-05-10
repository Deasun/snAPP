from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import report_bug, edit_bug, delete_bug, upvote_bug, get_bug_listing


urlpatterns = [
    url(r'^$', get_bug_listing, name='get_bug_listing'),
    url(r'^new/$', report_bug, name='report_bug'),
    url(r'^edit/(?P<id>\d+)$', edit_bug, name='edit_bug'),
    url(r'^delete/(?P<id>\d+)$', delete_bug, name='delete_bug'),
    url(r'^upvote/(?P<id>\d+)$', upvote_bug, name='upvote_bug'),
]


