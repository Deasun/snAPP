from django.shortcuts import render, redirect, get_object_or_404
from .models import FeatureTicket
from .forms import RequestFeatureForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.utils import timezone

@login_required
def request_feature(request):
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

# place request in shopping cart
# no posting until checkout - all part of this function
    else:
        request_form = RequestFeatureForm()
    return render(request, 'request_form.html', {'request_form': request_form})
   
    
@login_required
def upvote_feature(request, id=None):
    """
    Enable user to upvote a feature
    """
    feature = get_object_or_404(FeatureTicket, pk=id)
   
    """Prevent user upvoting own features"""
    if feature.created_by == request.user:
        messages.error(request, "You cannot upvote your own feature request. Visit our 'Developing the snAPP Commons' to find out how to promote your feature.")
    else: 
        user = request.user
        vote = feature.upvote(user)
    
        """Prevent double upvotes and validate upvotes"""
        if vote == 'already_upvoted':
            messages.success(request, "You have already upvoted this feature. Visit our 'Developing the snAPP Commons' to find out how to promote your feature.")
        else:
            messages.success(request, "Your upvote has been counted. Thanks. Visit our 'Developing the snAPP Commons' to find out how to promote your feature.")
             
    features = FeatureTicket.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, "feature_listing.html", {'feartures': features})


@login_required
def add_comment_to_feature(request, id):
    post = FeatureTicket.objects.filter(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            # comment.save()
            return redirect('feature_report', id=id)
    else:
        form = CommentForm()
    return render(request, "add_comments_to_feature_form.html", {'form': form})


@login_required
def feature_report(request, id):
    features = FeatureTicket.objects.filter(id=id)
    return render(request, "feature_report.html", {'features': features})


@login_required
def get_feature_listing(request):
    """
    List features that were reported prior to 'now' and render them to the 'feature_listing.html' template
    """
    features = FeatureTicket.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, "feature_listing.html", {'features': features})