from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from .choices import status_set
import datetime

"""
Feature Ticket model
"""
def default_status():
    return 'todo'

class FeatureTicket(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=False)
    links = models.URLField(blank=True)
    contribution = models.DecimalField(max_digits=8, decimal_places=3, default=9.99, blank=False)
    status = models.CharField(max_length=20, choices=status_set, default=default_status)
    
    def __str__(self):
	    return "Request: {} ({})".format(self.title, self.date_created)