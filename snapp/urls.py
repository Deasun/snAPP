from django.contrib import admin
from django.conf.urls import url, include 
from accounts import urls as urls_accounts
from bugtickets import urls as urls_bugtickets
from featuretickets import urls as urls_featuretickets
from search import urls as urls_search
from cart import urls as urls_cart
from accounts.views import index
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^bugtickets/', include(urls_bugtickets)),
    url(r'^featuretickets/', include(urls_featuretickets)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    
]


