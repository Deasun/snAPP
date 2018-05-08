from django.contrib import admin
from .models import BugTicket, RequestTicket

    
admin.site.register(BugTicket)
admin.site.register(RequestTicket)

