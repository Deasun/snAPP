from django.db import models
from django.contrib.auth.models import User
from .choices import ticket_type, status_set
import datetime

"""
Tickets model - for Bugs & Requests
"""

class BugTicket(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=False)

    def __str__(self):
	    return "{}: {} ({})".format(self.ticket, self.title, self.date_created)

class RequestTicket(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=False)
    links = models.URLField(blank=True)
    contribution = models.DecimalField(max_digits=6, decimal_places=2, min_value=9.99, blank=False)
    status = models.CharField(max_length=20, choices=status_set, default=default_status)
    
    def __str__(self):
	    return "{}: {} ({})".format(self.ticket, self.title, self.date_created)
	    
