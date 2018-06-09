from django.db import models, IntegrityError
from django.contrib.auth.models import User
from .choices import bugs
import datetime


    
"""
Bug Ticket model - enables users to report a bug
"""

class BugTicket(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bugs")
    date_created = models.DateField(null=True, default=datetime.date.today)
    date_started = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=False)
    bug_type = models.CharField(max_length=30, choices=bugs, blank=False)
    description = models.TextField(null=True, blank=False)
    report = models.TextField(null=True, blank=True)
    votes = models.IntegerField(default = 0)
    

    """Registers Upvotes from users by BugUpvote class and prevents self-votes"""
    def upvote(self, user):
        # pass
        try:
            self.bug_votes.create(bug_ticket=self, user=user, vote_type="up")
            self.votes += 1
            self.save()
        except IntegrityError:
            return 'already_upvoted'
    
    """Triggers bug status based on date_started and date_completed"""
    def status(self):
        # pass
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

    """Method to get BugTickets data for Daily, Weekly, Monthly Activity Line Chart"""
    @classmethod
    def qs_active_bugs(cls, num):
        # pass
        startdate = datetime.date.today()
        enddate = startdate - datetime.timedelta(days=num)
        active_bug_qs = BugTicket.objects.filter(date_started__range=(enddate, startdate))
        return active_bug_qs.count()    

    """Method to get BugTickets data for Daily, Weekly, Monthly Completion Line Chart"""
    @classmethod
    def qs_complete_bugs(cls, num):
        # pass
        startdate = datetime.date.today()
        enddate = startdate - datetime.timedelta(days=num)
        complete_bug_qs = BugTicket.objects.filter(date_completed__range=(enddate, startdate))
        return complete_bug_qs.count()
   
    """Method to count BugTickets by bug_type for Half-Pie Chart"""
    @classmethod
    def qs_by_bug_type(cls, bugtype):
        # pass
        qs_bug_type = BugTicket.objects.filter(bug_type=bugtype)
        return qs_bug_type.count()
        
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
    
    