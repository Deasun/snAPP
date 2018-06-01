from django.db import models, IntegrityError
from django.contrib.auth.models import User
import datetime
from .choices import feature_list

"""
Feature Ticket model
"""

class FeatureTicket(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_features")
    date_created = models.DateField(default=datetime.date.today)
    date_started = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=False)
    feature_type = models.CharField(max_length=30, choices=feature_list, blank=False)
    # Not currently in use - maintain for app development - enables non-paying members to support with 1 vote
    votes = models.IntegerField(default = 0)
    links = models.URLField(blank=True)
    contribution = models.DecimalField(max_digits=8, decimal_places=2, default=10.00, editable=False)    
    target = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    report = models.TextField(null=True, blank=False)
	 
    
    """
    Triggers feature status based on date_started and date_completed
    """

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

    
    """
    Method to get FeatureTickets data for Daily, Weekly, Monthly Activity Line Chart
    """
    @classmethod
    def qs_active_features(self, num):
        # pass
        startdate = datetime.date.today()
        enddate = startdate - datetime.timedelta(days=num)
        active_feature_qs = FeatureTicket.objects.filter(date_started__range=(enddate, startdate))
        return active_feature_qs.count()  

    
    """
    Method to get FeatureTickets data for Daily, Weekly, Monthly Completion Line Chart
    """
    @classmethod
    def qs_complete_features(self, num):
        # pass
        startdate = datetime.date.today()
        enddate = startdate - datetime.timedelta(days=num)
        complete_feature_qs = FeatureTicket.objects.filter(date_completed__range=(enddate, startdate))
        return complete_feature_qs.count()


    """
    Method to count FeatureTickets by bug_type for Half-Pie Chart
    """
    @classmethod
    def qs_by_feature_type(self, featuretype):
        # pass
        qs_feature_type = FeatureTicket.objects.filter(feature_type=featuretype)
        return qs_feature_type.count()

    
    """
    String Representation
    """
    def __str__(self):
	    return "Request: {} ({})".format(self.title, self.date_created)



"""
Comment Model - enables user to leave comments on feature requests
"""

class Comment(models.Model):
    feature_ticket = models.ForeignKey(FeatureTicket, on_delete=models.CASCADE, related_name="feature_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="comment_author")
    text = models.TextField()
    date_created = models.DateField(default=datetime.date.today)

    
    def __str__(self):
        return "{}: {}'s COMMENTS".format(self.feature_ticket, self.author)