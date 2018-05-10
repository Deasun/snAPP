from django.db import models
from django.contrib.auth.models import User
from bugtickets.models import BugTicket
import datetime

"""
BugUpvote Model - enables user to upvote bug reports
"""

class BugUpvote(models.Model):
    bug_ticket = models.ForeignKey(BugTicket, on_delete=models.CASCADE, related_name="bugs_votes")
    user = models.ForeignKey(User, related_name="user_votes", on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)
    vote_type = models.CharField(max_length=10, blank=False)

    
    class Meta:
        unique_together = ('bug_ticket', 'user', 'date_created', 'vote_type')
    
    def __str__(self):
	    return "{} upvoted {} ({})".format(self.user, self.bugticket, self.date_created)
