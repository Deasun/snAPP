from django.shortcuts import render, redirect, get_object_or_404
from .models import FeatureTicket
from .forms import RequestFeatureForm
from django.contrib.auth.decorators import login_required

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
            return redirect('profile')
            
    else:
        request_form = RequestFeatureForm()
    return render(request, 'request_form.html', {'request_form': request_form})