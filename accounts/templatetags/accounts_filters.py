from django import template
from datetime import date, timedelta

register = template.Library()


@register.filter(name='assess_alert_date')
def assess_alert_date(value):
    delta = value - date.today()
    
    if delta.days < 1:
        return "expired"
    
    else:
        return "active"