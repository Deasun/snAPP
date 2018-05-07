from django.db import models
from accounts.models import Profile
from .choices import ticket_type
import datetime

"""
Tickets model - for Bugs & Requests
"""
def default_status():
    return "Pending"
    
class Tickets(models.Model):
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)
    ticket = models.CharField(max_length=15, choices=ticket_type, blank=False)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=False)
    status = models.CharField(max_length=20, default=default_status)
    
    def __str__(self):
	    return "{}: {} ({})".format(self.ticket, self.title, self.date_created)
	    
