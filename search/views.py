from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib import messages
from featuretickets.models import FeatureTicket
from featuretickets.charts import config_featurepie_chart, config_featureline_chart
from bugtickets.models import BugTicket
from bugtickets.charts import config_bugline_chart, config_bugpie_chart, config_bugbar_chart
from django.contrib.auth.models import User
from accounts.models import Profile





@login_required
def feature_search(request):
    features = FeatureTicket.objects.filter(feature_type__icontains=request.GET['q'])
    
    # Handle empty query set with django message 
    if not features:
        messages.success(request, "Your search returned no results. Please try again.")
    
    """Pyagl chart data for features"""
    feature_line_data = config_featureline_chart()
    feature_pie_data = config_featurepie_chart()
    
    # Pass data to render charts
    return render(request, 'feature_listing.html', {
                'features': features, 
                'feature_line_data': feature_line_data, 
                'feature_pie_data': feature_pie_data
                })

@login_required
def bug_search(request):
    bugs = BugTicket.objects.filter(description__icontains=request.GET['q'])
    
    # Handle empty query set with django message 
    if not bugs:
        messages.success(request, "Your search returned no results. Please try again.")
    
    bug_line_data = config_bugline_chart()
    bug_pie_data = config_bugpie_chart()
    bug_bar_data = config_bugbar_chart()
    
    # Pass data to render charts
    return render(request, 'bug_listing.html', {
                'bugs': bugs, 
                'bug_line_data': bug_line_data, 
                'bug_pie_data': bug_pie_data,
                'bug_bar_data': bug_bar_data,
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

# search for keyword in alert
@login_required
def alert_search(request):
    alerts = Profile.objects.filter(alert__icontains=request.GET['q'])
    
    # Handle empty query set with django message 
    if not alerts:
        messages.success(request, "Your search returned no results. Please try again.")
    
    user = request.user
    auth_user = request.user
    bugs = BugTicket.objects.filter(created_by=user.id)
    features = FeatureTicket.objects.filter(created_by=user.id)
    return render(request, 'profile.html', {
                "features": features, 
                "bugs": bugs, 
                "user": user, 
                "auth_user": auth_user, 
                "alerts": alerts,
                })
        
    
