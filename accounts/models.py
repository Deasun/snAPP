from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime



"""
Profile model - extra information relating to User Model
"""
class Profile(models.Model):
	# user to to null=True and models.SET_NULL to prevent related objects being deleted if Profile deleted
	user = models.OneToOneField(User, unique=True, null=True, on_delete=models.SET_NULL)
	image = models.ImageField(upload_to='images', default='images/group-white_eSru9tk.png')
	trade_union = models.CharField(null=True, max_length=100, default='')
	description = models.TextField(null=True, default='No profile description provided.')
	alert = models.TextField(null=True, default='No active alerts.')
	alert_date = models.DateField(null=True, default=datetime.date.today)

	
	def __str__(self):
	    return "{}'s profile".format(self.user)
	
