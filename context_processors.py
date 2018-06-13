from accounts.models import Profile


def get_random_alert(request):
    profile = Profile.objects.all().order_by('?')[:1]
    return {"profile": profile }