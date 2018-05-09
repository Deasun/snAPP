from django.db import models
from django.contrib.auth.models import User
from .choices import status_set
import datetime

"""
Bug Ticket model
"""
def default_status():
    return 'todo'

class BugTicket(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=False)
    status = models.CharField(max_length=20, choices=status_set, default=default_status)


    def __str__(self):
	    return "Bug: {} ({} - {})".format(self.title, self.date_created, self.id)