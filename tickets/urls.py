from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^create_ticket/$', create_ticket, name="create_ticket"),
]