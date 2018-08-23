from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.contrib import messages
from featuretickets.models import FeatureTicket
from featuretickets.charts import config_featurepie_chart, config_featureline_chart
from bugtickets.models import BugTicket
from bugtickets.charts import config_bugline_chart, config_bugpie_chart, config_bugbar_chart
from django.contrib.auth.models import User
from accounts.models import Profile


@login_required
def feature_search(request):
    """
    Enable full-text search of featureticket title, description and type
    """
    features = FeatureTicket.objects.annotate(
        search=SearchVector('title', 'description', 'feature_type'),
        ).filter(search=request.GET['q'])
    
    # Handle empty query set with django message 
    if not features:
        messages.success(request, "Your search returned no results. Please try again.")
    
    """Pyagl chart data for snAPP admin activity on features and member requests"""
    feature_line_data = config_featureline_chart()
    feature_pie_data = config_featurepie_chart()
    
    return render(request, 'feature_listing.html', {
                'features': features, 
                'feature_line_data': feature_line_data, 
                'feature_pie_data': feature_pie_data
                })


@login_required
def bug_search(request):
    """
    Enable user to search snAPP bugs by title, description and type
    """
    bugs = BugTicket.objects.annotate(
        search=SearchVector('title', 'description', 'bug_type'),
        ).filter(search=request.GET['q'])
    
    # Handle empty query set with django message 
    if not bugs:
        messages.success(request, "Your search returned no results. Please try again.")
    
    """Pyagl chart data for snAPP admin activity on bugs and member bug reports"""
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


@login_required
def member_search(request):
    """
    Enable users to search for other snAPP member profiles by username
    """
  
    member = request.GET['member']
    try:
        user = User.objects.get(username=member)
        return redirect('profile', id=user.id)
    
    except ObjectDoesNotExist:
         messages.success(request, "There are no snAPP members with that username. Please try again.")
         return redirect('profile', id=request.user.id)


@login_required
def alert_search(request):
    """
    Enable users to search snAPP alerts by keyword
    """

    alerts = Profile.objects.annotate(
        search=SearchVector('alert'),
        ).filter(search=request.GET['q'])
    
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