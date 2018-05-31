from django.shortcuts import render
from featuretickets.models import FeatureTicket
from featuretickets.charts import feature_chart_data, feature_pie_chart_data
from bugtickets.models import BugTicket
from bugtickets.charts import chart_data, pie_chart_data



def feature_search(request):
    features = FeatureTicket.objects.filter(description__icontains=request.GET['q'])
    return render(request, 'feature_listing.html', {'features': features, 'feature_chart_data': feature_chart_data, 'feature_pie_chart_data': feature_pie_chart_data})

def bug_search(request):
    bugs = BugTicket.objects.filter(description__icontains=request.GET['q'])
    bug_votes = BugTicket.objects.all().order_by('-votes')[:3]
    return render(request, 'bug_listing.html', {'bugs': bugs,'bug_votes': bug_votes, 'chart_data': chart_data, 'pie_chart_data': pie_chart_data })
