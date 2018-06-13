from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from featuretickets.models import FeatureTicket
from featuretickets.charts import feature_chart_data, feature_pie_chart_data
from bugtickets.models import BugTicket
from bugtickets.charts import chart_data, pie_chart_data, bar_chart_data



def feature_search(request):
    features = FeatureTicket.objects.filter(feature_type__icontains=request.GET['q'])
    
    # Handle empty query set with django message 
    if not bugs:
        messages.success(request, "Your search returned no results. Please try again.")
    
    # Pass data to render charts
    return render(request, 'feature_listing.html', {
                'features': features, 
                'feature_chart_data': feature_chart_data, 
                'feature_pie_chart_data': feature_pie_chart_data
                })

def bug_search(request):
    bugs = BugTicket.objects.filter(description__icontains=request.GET['q'])
    
    # Handle empty query set with django message 
    if not bugs:
        messages.success(request, "Your search returned no results. Please try again.")
    
    # Pass data to render charts
    return render(request, 'bug_listing.html', {
                'bugs': bugs, 
                'chart_data': chart_data, 
                'pie_chart_data': pie_chart_data,
                'bar_chart_data': bar_chart_data
                 })
