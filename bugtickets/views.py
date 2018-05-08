from django.shortcuts import render, redirect, get_object_or_404
from .models import BugTicket
from .forms import ReportBugForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def report_bug(request):
    """
    Create or edit a Bug Report ticket
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
def get_bug_listing(request):
    """
    List bugs that were reported prior to 'now'
    and render them to the 'bug_listing.html'
    template
    """
    
    bugs = BugTicket.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, "bug_listing.html", {'bugs': bugs})