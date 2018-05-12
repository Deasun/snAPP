from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import get_feature_listing, request_feature, upvote_bug, bug_report, add_comment_to_bug

urlpatterns = [
    url(r'^$', get_feature_listing, name='get_feature_listing'),
    url(r'^new/$', request_feature, name='request_feature'),
    url(r'^upvote/(?P<id>\d+)$', upvote_bug, name='upvote_bug'),
    url(r'^bug/(?P<id>\d+)$', bug_report, name='bug_report'),
    url(r'^bug/(?P<id>\d+)/comment$', add_comment_to_bug, name='add_comment_to_bug'),
]