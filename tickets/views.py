from django.shortcuts import render, redirect, get_object_or_404
from .models import Tickets
from .forms import ReportBugForm, RequestFeatureForm
from django.contrib.auth.decorators import login_required

@login_required
def report_bug(request):
    """
    Create a new ticket existing one
    """
    if request.method == 'POST':
        report_form = ReportBugForm(request.POST, request.FILES)
        if report_form.is_valid():
            submit = report_form.save(commit=False)
            submit.created_by = request.user
            return redirect('profile')
            
    else:
        report_form = ReportBugForm()
    return render(request, 'report_form.html', {'report_form': report_form})


@login_required
def request_feature(request):
    """
    Create a new ticket existing one
    """
    if request.method == 'POST':
        request_form = RequestFeatureForm(request.POST, request.FILES)
        if request_form.is_valid():
            submit = request_form.save(commit=False)
            submit.created_by = request.user
            return redirect('profile')
            
    else:
        request_form = RequestFeatureForm()
    return render(request, 'request_form.html', {'request_form': request_form})


# def toggle_status(request, id):



# def make_feature_request(request):
