from django.db import models, IntegrityError
from django.contrib.auth.models import User
from .choices import bugs
import datetime


    
"""
Bug Ticket model - enables users to report a bug
"""

class BugTicket(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bugs")
    date_created = models.DateField(default=datetime.date.today)
    date_started = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=False)
    bug_type = models.CharField(max_length=30, choices=bugs, blank=False)
    description = models.TextField(null=True, blank=False)
    votes = models.IntegerField(default = 0)
    

    """
    Registers Upvotes from users by BugUpvote class and prevents self-votes
    """
    def upvote(self, user):
        try:
            self.bug_votes.create(bug_ticket=self, user=user, vote_type="up")
            self.votes += 1
            self.save()
        except IntegrityError:
            return 'already_upvoted'
    
   
    """
    Triggers bug status based on date_started and date_completed
    """
    def status(self):
        try:
            if self.date_started == None and self.date_completed == None:
                return '--'
            elif self.date_started != None and self.date_completed != None:
                return 'complete'
            elif self.date_started == None and self.date_completed != None:
                return 'complete'
            else:
                return 'active'
                
        except IntegrityError:
            return 'Unknown status'

    """
    Class methods to get BugTickets data for Daily, Weekly, Monthly Activity Chart
    """
    @classmethod
    def qs_today_active_bugs(self):
        startdate = datetime.date.today()
        active_bug_today_qs = BugTicket.objects.filter(date_started=datetime.date.today())
        return active_bug_today_qs.count()    
    
    @classmethod
    def qs_7_day_active_bugs(self):
        startdate = datetime.date.today()
        last_week = startdate - datetime.timedelta(days=7)
        active_bug_7_qs = BugTicket.objects.filter(date_started__range=(last_week, startdate))
        return active_bug_7_qs.count()    
    
    @classmethod
    def qs_30_day_active_bugs(self):
        startdate = datetime.date.today()
        last_month = startdate - datetime.timedelta(days=30)
        active_bug_30_qs = BugTicket.objects.filter(date_started__range=(last_month, startdate))
        return active_bug_30_qs.count()

    """
    Class methods to get BugTickets data for Daily, Weekly, Monthly Completion Chart
    """
    @classmethod
    def qs_today_complete_bugs(self):
        startdate = datetime.date.today()
        complete_bug_today_qs = BugTicket.objects.filter(date_completed=datetime.date.today())
        return complete_bug_today_qs.count()    
    
    @classmethod
    def qs_7_day_complete_bugs(self):
        startdate = datetime.date.today()
        last_week = startdate - datetime.timedelta(days=7)
        complete_bug_7_qs = BugTicket.objects.filter(date_completed__range=(last_week, startdate))
        return complete_bug_7_qs.count()    
    
    @classmethod
    def qs_30_day_complete_bugs(self):
        startdate = datetime.date.today()
        last_month = startdate - datetime.timedelta(days=30)
        complete_bug_30_qs = BugTicket.objects.filter(date_completed__range=(last_month, startdate))
        return complete_bug_30_qs.count()


    """
    String Representation
    """
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
	    return "({})".format(self.date_created)

"""
Comment Model - enables user to leave comments on bug reports
"""
class Comment(models.Model):
    bug_ticket = models.ForeignKey(BugTicket, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user_author")
    text = models.TextField()
    date_created = models.DateField(default=datetime.date.today)

    
    def __str__(self):
	    return "({})".format(self.date_created)
    
    