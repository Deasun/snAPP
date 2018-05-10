from django.contrib import admin
from .models import BugTicket, BugUpvote

    
admin.site.register(BugTicket)
admin.site.register(BugUpvote)