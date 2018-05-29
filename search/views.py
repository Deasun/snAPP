from django.shortcuts import render
from featuretickets.models import FeatureTicket
from bugtickets.models import BugTicket
from bugtickets.charts import chart_data

def feature_search(request):
    features = FeatureTicket.objects.filter(description__icontains=request.GET['q'])
    return render(request, 'feature_listing.html', {'features': features})

def bug_search(request):
    bugs = BugTicket.objects.filter(description__icontains=request.GET['q'])
    return render(request, 'bug_listing.html', {'bugs': bugs, 'chart_data': chart_data })
