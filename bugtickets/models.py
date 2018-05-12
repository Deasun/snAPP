from django.db import models, IntegrityError
from django.contrib.auth.models import User
from .choices import status_set
import datetime

"""
Bug Ticket model - enables users to report a bug
"""
def default_status():
    return 'todo'

class BugTicket(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bugs")
    date_created = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=False)
    votes = models.IntegerField(default = 0)
    status = models.CharField(max_length=20, choices=status_set, default=default_status)

    def upvote(self, user):
        
        try:
            self.bug_votes.create(bug_ticket=self, user=user, vote_type="up")
            self.votes += 1
            self.save()
        except IntegrityError:
            return 'already_upvoted'

    def __str__(self):
	    return "Bug: {} ({} - {})".format(self.title, self.date_created, self.id)


"""
BugUpvote Model - enables user to upvote bug reports
"""

class BugUpvote(models.Model):
    bug_ticket = models.ForeignKey(BugTicket, on_delete=models.CASCADE, related_name="bug_votes")
    user = models.ForeignKey(User, related_name="user_votes", on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)
    vote_type = models.CharField(max_length=10, blank=False)

    
    class Meta:
        unique_together = ('bug_ticket', 'user', 'vote_type')
    
    def __str__(self):
	    return "{} UPVOTED {}, DATE: ({})".format(self.user, self.bug_ticket, self.date_created)

"""
Comment Model - enables user to leave comments on bug reports
"""
class Comment(models.Model):
    bug_ticket = models.ForeignKey(BugTicket, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_author")
    text = models.TextField()
    date_created = models.DateField(default=datetime.date.today)

    
    def __str__(self):
        return "{}: {}'s COMMENTS".format(self.bug_ticket, self.author)
    
    