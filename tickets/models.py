from django.db import models
from .models import Profile
import datetime

"""
Tickets model - for Bugs & Requests
"""
def default_status():
    return "Pending"
    
class Tickets(models.Model):
    created_by = models.ForeignKey(Profile, null=False)
    date_created = models.DateField(default=datetime.date.today)
    ticket_type = models.BooleanField(blank=False, default=False)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default=default_status)
    
    def __str__(self):
	    return self.title