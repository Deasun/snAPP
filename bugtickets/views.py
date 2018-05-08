from django.shortcuts import render, redirect, get_object_or_404
from .models import BugTicket
from .forms import ReportBugForm
from django.contrib.auth.decorators import login_required

@login_required
def report_bug(request):
    """
    Create a new Bug Report ticket
    """
    if request.method == 'POST':
        report_form = ReportBugForm(request.POST, request.FILES)
        if report_form.is_valid():
            submit = report_form.save(commit=False)
            submit.created_by = request.user
            submit.save()
            return redirect('profile')
            
    else:
        report_form = ReportBugForm()
    return render(request, 'report_form.html', {'report_form': report_form})