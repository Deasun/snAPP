from django.shortcuts import render, redirect, get_object_or_404
from .models import FeatureTicket
from checkout.models import OrderLineItem   
from .forms import RequestFeatureForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import auth, messages
from django.utils import timezone

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
            return redirect('profile')

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
    print(orders)
    return render(request, "feature_report.html", {'features': features, 'orders': orders })


@login_required
def get_feature_listing(request):
    """
    List features ranked by most recent date and render them to the 'feature_listing.html' template
    """
    features = FeatureTicket.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, "feature_listing.html", {'features': features })