from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import BugTicket, BugUpvote, Comment
from .forms import ReportBugForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from  django.contrib.messages import success, warning, error
from django.utils import timezone
import datetime
from bugtickets.charts import config_bugline_chart, config_bugpie_chart, config_bugbar_chart

import pygal
from pygal.style import Style
from .models import BugTicket


@login_required
def report_bug(request, pk=None):
    """
    Create a Bug Report ticket
    """
    if request.method == 'POST':
        report_form = ReportBugForm(request.POST, request.FILES)
        if report_form.is_valid():
            submit = report_form.save(commit=False)
            submit.created_by = request.user
            submit.save()
            return redirect('get_bug_listing')
    else:
        report_form = ReportBugForm()
    return render(request, 'report_form.html', {'report_form': report_form})


@login_required
def upvote_bug(request, id=None):
    """
    Enable user to upvote a bug and render line chart data
    """
    bug = get_object_or_404(BugTicket, pk=id)
   
    """Prevent user upvoting own reports"""
    if bug.created_by == request.user:
        messages.error(request, "You cannot upvote your own bug report.")
    else: 
        user = request.user
        vote = bug.upvote(user)
    
        """Prevent double upvotes and validate upvotes"""
        if vote == 'already_upvoted':
            messages.success(request, "You have already upvoted this ticket.")
        else:
            messages.success(request, "Your upvote has been counted. Thanks")
    
    bugs = BugTicket.objects.filter(pk=id)
    return render(request, "bug_report.html", {'bugs': bugs})


@login_required
def add_comment_to_bug(request, pk):
    """
    Enable user to add comments to bug reports
    """
    post = BugTicket.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.bug_ticket = post
            comment.author = request.user
            comment.save()
            return redirect('bug_report', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "add_comments_to_bug_form.html", {'form': form, 'post': post})


@login_required
def bug_report(request, pk=id):
    """
    Enable user to report a bug_report
    """
    bugs = BugTicket.objects.filter(id=pk)
    
    # return message if bug does not exist
    if not bugs:
            messages.success(request, "There is no bug with that identity. Please search again.")
            return redirect('get_bug_listing')
    else:
        return render(request, "bug_report.html", {'bugs': bugs})


@login_required
def get_bug_listing(request):
    """
    List bugs with most recent on top and render chart data
    """
    
    """order bugs by date reported"""
    bugs = BugTicket.objects.filter(date_created__lte=timezone.now()).order_by('-date_created')
    
    """retrieve data on snAPP admin activity for charts"""
    bug_line_data = config_bugline_chart()
    bug_pie_data = config_bugpie_chart()
    bug_bar_data = config_bugbar_chart()
    
    return render(request, "bug_listing.html", {
            'bugs': bugs, 
            'bug_line_data': bug_line_data, 
            'bug_pie_data': bug_pie_data,
            'bug_bar_data': bug_bar_data,
    })