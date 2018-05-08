from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import request_feature


urlpatterns = [
    url(r'^request_feature/$', request_feature, name="request_feature"),
]