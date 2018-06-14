from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib import messages
from featuretickets.models import FeatureTicket
from featuretickets.charts import feature_chart_data, feature_pie_chart_data
from bugtickets.models import BugTicket
from bugtickets.charts import chart_data, pie_chart_data, bar_chart_data
from django.contrib.auth.models import User
from accounts.models import Profile





@login_required
def feature_search(request):
    features = FeatureTicket.objects.filter(feature_type__icontains=request.GET['q'])
    
    # Handle empty query set with django message 
    if not features:
        messages.success(request, "Your search returned no results. Please try again.")
    
    # Pass data to render charts
    return render(request, 'feature_listing.html', {
                'features': features, 
                'feature_chart_data': feature_chart_data, 
                'feature_pie_chart_data': feature_pie_chart_data
                })

@login_required
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


# search for snAPP member profile (by username)
@login_required
def member_search(request):
    member = request.GET['member']
    
    try:
        user = User.objects.get(username=member)
        return redirect('profile', id=user.id)
    except ObjectDoesNotExist:
         messages.success(request, "There are no snAPP members with that username. Please try again.")
         return redirect('profile', id=request.user.id)
        # raise Http404("There are no snAPP members with that username.")

  
        
    
