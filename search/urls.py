from django.urls import include, path
from .views import feature_search, bug_search, alert_search, member_search

urlpatterns = [
    path('feature/', feature_search, name='feature_search'),
    path('bug/', bug_search, name='bug_search'),
    path('alert/', alert_search, name='alert_search'),
    path('member_search/', member_search, name="member_search")
    ]