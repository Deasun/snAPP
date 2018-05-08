from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import report_bug, get_bug_listing


urlpatterns = [
    url(r'^$', get_bug_listing, name='get_bug_listing'),
    url(r'^new/$', report_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit/$', report_bug, name='edit_bug')
]