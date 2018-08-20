from django.contrib import admin
from django.urls import path, include 
from accounts import urls as urls_accounts
from bugtickets import urls as urls_bugtickets
from featuretickets import urls as urls_featuretickets
from checkout import urls as urls_checkout
from search import urls as urls_search
from cart import urls as urls_cart
from accounts.views import index
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('accounts/', include(urls_accounts)),
    path('bugtickets/', include(urls_bugtickets)),
    path('featuretickets/', include(urls_featuretickets)),
    path('cart/', include(urls_cart)),
    path('search/', include(urls_search)),
    path('checkout/', include(urls_checkout)),
    path('media/(<path>)', static.serve, {'document_root': MEDIA_ROOT}),
]
