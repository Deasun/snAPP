from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime



"""
Profile model - extra information relating to User Model
"""
class Profile(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
	image = models.ImageField(null=True, upload_to='images', default='')
	trade_union = models.CharField(null=True, max_length=100, default='')
	description = models.TextField(null=True, default='')
	alert = models.TextField(null=True, default='')
	alert_date = models.DateField(null=True, default=datetime.date.today)

	def __str__(self):
	    return "{}'s profile".format(self.user)
	
