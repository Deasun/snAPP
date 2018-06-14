from django.conf.urls import url
from .views import feature_search, bug_search, alert_search, member_search

urlpatterns = [
    url(r'^feature/$', feature_search, name='feature_search'),
    url(r'^bug/$', bug_search, name='bug_search'),
    url(r'^alert/$', alert_search, name='alert_search'),
    url(r'^member_search/$', member_search, name="member_search")
    ]