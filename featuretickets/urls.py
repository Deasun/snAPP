from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import get_feature_listing, request_feature, feature_report, add_comment_to_feature

urlpatterns = [
    path('', get_feature_listing, name='get_feature_listing'),
    path('new/', request_feature, name='request_feature'),
    path('feature/<int:pk>', feature_report, name='feature_report'),
    path('feature/<int:pk>/comment', add_comment_to_feature, name='add_comment_to_feature'),
]