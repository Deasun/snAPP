from django import template
from django.template import Library
from accounts.models import Profile
     
register = Library()
     
@register.simple_tag
def random_alert():
    profile = Profile.objects.all().order_by('?')[:1]
    return profile
    