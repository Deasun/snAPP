from django.conf.urls import url
from .views import bug_search, feature_search

urlpatterns = [
    url(r'^$', bug_search, name='bug_search'),
    url(r'^$', feature_search, name='feature_search'),
    ]