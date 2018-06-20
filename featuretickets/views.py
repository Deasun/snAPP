from django.shortcuts import render, redirect, get_object_or_404
from .models import FeatureTicket
from accounts.models import Profile
from checkout.models import Order, OrderLineItem  
from .forms import RequestFeatureForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Max
from django.contrib import auth, messages
from django.utils import timezone
from .charts import config_featureline_chart, config_featurepie_chart



@login_required
def request_feature(request, pk=None):
    """
    Create a new Feature Request ticket
    """
    if request.method == 'POST':
        request_form = RequestFeatureForm(request.POST, request.FILES)
        if request_form.is_valid():
            submit = request_form.save(commit=False)
            submit.created_by = request.user
            submit.save()
            messages.success(request, "Excellent. Your feature request will be posted to start attracting supporters once you have made your snAPP contribution!")
            return redirect('get_feature_listing')

    else:
        request_form = RequestFeatureForm()
    return render(request, 'request_form.html', {'request_form': request_form})
   

@login_required
def add_comment_to_feature(request, pk):
    """
    Enable user to add a comment to a feature request
    """
    
    post = FeatureTicket.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.feature_ticket = post
            comment.author = request.user
            comment.save()
            return redirect('feature_report', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "add_comments_to_feature_form.html", {'form': form, 'post': post})


@login_required
def feature_report(request, pk=id):
    """
    Display Feature Report
    """
    
    features = FeatureTicket.objects.filter(id=pk)
    
    # return message if bug does not exist
    if not features:
        messages.success(request, "That feature does not exist. Please search again.")
        return redirect('get_feature_listing') 
 
    else:
        """Query OrderLineItem quantity to render upvotes"""
        def feature_upvotes():
            orders = OrderLineItem.objects.filter(feature=pk).aggregate(Sum('quantity'))
            for k,v in orders.items():
                ticket_total = v
                return ticket_total
        
        total = feature_upvotes()

    return render(request, "feature_report.html", {'features': features, 'total': total})


@login_required
def get_feature_listing(request):
    """
    Display information on feature requests
    """
    
    """List features ranked by most recent date and render them to the 'feature_listing.html' template"""
    features = FeatureTicket.qs_desc_date()  
    
    """Pyagl chart data for snAPP admin activity on features"""
    feature_line_data = config_featureline_chart()
    feature_pie_data = config_featurepie_chart()
    
    """Retrieve chart data on latest features by status"""
    latest_feature = FeatureTicket.qs_latest_complete_feature()
    next_feature = FeatureTicket.qs_latest_active_feature()
    random_feature = FeatureTicket.qs_random_requested_feature()
    
    return render(request, 'feature_listing.html', {
                'features': features, 
                'feature_line_data': feature_line_data, 
                'feature_pie_data': feature_pie_data, 
                'latest_feature': latest_feature, 
                'next_feature': next_feature, 
                'random_feature': random_feature })
    
