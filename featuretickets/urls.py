from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import get_feature_listing, request_feature, upvote_feature, feature_report, add_comment_to_feature

urlpatterns = [
    url(r'^$', get_feature_listing, name='get_feature_listing'),
    url(r'^new/$', request_feature, name='request_feature'),
    url(r'^upvote/(?P<id>\d+)$', upvote_feature, name='upvote_feature'),
    url(r'^feature/(?P<pk>\d+)$', feature_report, name='feature_report'),
    url(r'^feature/(?P<pk>\d+)/comment$', add_comment_to_feature, name='add_comment_to_feature'),
]