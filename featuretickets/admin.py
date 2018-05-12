from django.contrib import admin
from .models import FeatureTicket, FeatureUpvote, Comment

    
admin.site.register(FeatureTicket)
admin.site.register(FeatureUpvote)
admin.site.register(Comment)