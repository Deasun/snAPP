from django.contrib.auth import views as auth_views
from django.conf.urls import url
from .views import report_bug


urlpatterns = [
    url(r'^report_bug/$', report_bug, name="report_bug"),
]