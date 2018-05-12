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
    contribution = models.DecimalField(max_digits=8, decimal_places=2, default=9.99, blank=False)
    total_contributions = models.DecimalField(max_digits=8, decimal_places=2, default=9.99, blank=False)
    status = models.CharField(max_length=20, choices=status_set, default=default_status)
    
    def __str__(self):
	    return "Request: {} ({})".format(self.title, self.date_created)


"""
FeatureUpvote Model - enables user to upvote feature requests
"""

class FeatureUpvote(models.Model):
    feature_ticket = models.ForeignKey(FeatureTicket, on_delete=models.CASCADE, related_name="feature_votes")
    user = models.ForeignKey(User, related_name="feature_votes", on_delete=models.CASCADE)
    date_created = models.DateField(default=datetime.date.today)
    vote_type = models.CharField(max_length=10, blank=False)

    
    class Meta:
        unique_together = ('feature_ticket', 'user', 'vote_type')
    
    def __str__(self):
	    return "{} UPVOTED {}, DATE: ({})".format(self.user, self.feature_ticket, self.date_created)

"""
Comment Model - enables user to leave comments on feature requests
"""
class Comment(models.Model):
    feature_ticket = models.ForeignKey(FeatureTicket, on_delete=models.CASCADE, related_name="feature_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    text = models.TextField()
    date_created = models.DateField(default=datetime.date.today)

    
    def __str__(self):
        return "{}: {}'s COMMENTS".format(self.feature_ticket, self.author)