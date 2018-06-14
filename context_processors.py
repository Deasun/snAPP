from accounts.models import Profile
from datetime import date, datetime


# get random valid alerts
def get_random_alert(request):
    today = datetime.today()
    profile = Profile.objects.filter(alert_date__gte=today).order_by('?')[:1]
    return {"profile": profile }