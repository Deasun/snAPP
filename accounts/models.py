from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# # Profile model - extra information relating to User Model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images',null=True, blank=True)
	trade_union = models.CharField(max_length=100, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
	    return "Profile of user {}".format(self.user.username)
