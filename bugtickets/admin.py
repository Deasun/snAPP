from django.contrib import admin
from .models import BugTicket, BugUpvote, Comment

    
admin.site.register(BugTicket)
admin.site.register(BugUpvote)
admin.site.register(Comment)