from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^report_bug/$', report_bug, name="report_bug"),
    url(r'^request_feature/$', request_feature, name="request_feature"),
]