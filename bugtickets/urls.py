from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import report_bug, upvote_bug, get_bug_listing, add_comment_to_bug, bug_report
from . import api_views


urlpatterns = [
    # path(r'^$', get_bug_listing, name='get_bug_listing'),
    path('', get_bug_listing, name='get_bug_listing'),
    path('new/', report_bug, name='report_bug'),
    path('upvote/<int:id>', upvote_bug, name='upvote_bug'),
    path('bug/<int:pk>', bug_report, name='bug_report'),
    path('bug/<int:pk>/comment', add_comment_to_bug, name='add_comment_to_bug'),
    path('api_views/', api_views.BugTicketViewSet.as_view())
]


