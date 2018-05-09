from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import BugTicket
from .forms import ReportBugForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

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
def edit_bug(request, id):
    """
    Edit a Bug Report ticket
    """
    submit = get_object_or_404(BugTicket, pk=id)
    
    # Is this required? Double protection - also in template
    """Enable authors only to edit bugs"""
    if submit.created_by != request.user:
        messages.warning(request, "You cannot edit a bug report that you did not generate.")
    
    else:    
        if request.method == 'POST':
            report_form = ReportBugForm(request.POST, instance=submit)
            if report_form.is_valid():
                submit = report_form.save(commit=False)
                submit.created_by = request.user
                submit.save()
                return redirect('get_bug_listing')
                    
        else:
            report_form = ReportBugForm(instance=submit)
    
    return render(request, 'report_form.html', {'report_form': report_form})


@login_required
def delete_bug(request, id=None):
    query = BugTicket.objects.get(id=id)
    query.delete()
    return render(request, "bug_listing.html")
    


@login_required
def get_bug_listing(request):
    """
    List bugs that were reported prior to 'now'
    and render them to the 'bug_listing.html'
    template
    """
    bugs = BugTicket.objects.filter(date_created__lte=timezone.now()).order_by('date_created')
    return render(request, "bug_listing.html", {'bugs': bugs})