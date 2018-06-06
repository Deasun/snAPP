from django.shortcuts import render, redirect, get_object_or_404
from .models import FeatureTicket
from accounts.models import Profile
from checkout.models import Order, OrderLineItem   
from .forms import RequestFeatureForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Max
from django.contrib import auth, messages
from django.utils import timezone
from .charts import feature_chart_data, feature_pie_chart_data

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
    return render(request, "add_comments_to_feature_form.html", {'form': form})


@login_required
def feature_report(request, pk=id):
    features = FeatureTicket.objects.filter(id=pk)
    
    # Query OrderLineItem quantity to render upvotes
    orders = OrderLineItem.objects.filter(feature=pk).aggregate(Sum('quantity'))
    
    return render(request, "feature_report.html", {'features': features, 'orders': orders})


@login_required
def get_feature_listing(request):
    """
    List features & purchases ranked by most recent date and render them to the 'feature_listing.html' template
    """
    # Class method for rendering FeatureTicket table ordered by date
    features = FeatureTicket.qs_desc_date()  
    
    # Class methods for rendering latest features
    latest_feature = FeatureTicket.qs_latest_complete_feature()
    next_feature = FeatureTicket.qs_latest_active_feature()
    random_feature = FeatureTicket.qs_random_requested_feature()
    
    return render(request, 'feature_listing.html', {'features': features, 'feature_chart_data': feature_chart_data, 'feature_pie_chart_data': feature_pie_chart_data, 'latest_feature': latest_feature, 'next_feature': next_feature, 'random_feature': random_feature })
    
    

