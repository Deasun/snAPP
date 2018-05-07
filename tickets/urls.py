from django.conf.urls import url, include
from tickets.views import create_or_edit_ticket


urlpatterns = [
    url(r'^create_or_edit_ticket/', create_or_edit_ticket, name="create_or_edit_ticket"),
]