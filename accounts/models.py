from django.db import models
from datetime import date

# User Profile model
# Once signed-in create edit function
class UserProfile(models.Model):
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	username = models.CharField(max_length=30)
	email = models.EmailField()
	image = models.ImageField(upload_to='images', blank=True)
	description = models.TextField(blank=True)
	join_date = models.DateField(default=date.today)
	password1 = models.CharField(max_length=50)
	password2 = models.CharField(max_length=50)

	def __str__(self):
	    return '%s - %s - %s' % (self.username, self.email, self.join_date)
	   # Test the __str__
	   # Test blank fields & error returns