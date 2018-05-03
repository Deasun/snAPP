from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver








# # Profile model - extra information relating to User Model
# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	image = models.ImageField(upload_to='images', blank=True)
# 	description = models.TextField(blank=True)

# 	def __str__(self):
# 	    return self.description
	    
# # Profile model created/updated when User instance created/updated
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()