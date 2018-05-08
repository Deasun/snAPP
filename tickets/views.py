from django.shortcuts import render, redirect, get_object_or_404
from .models import Tickets
from .forms import TicketForm
from django.contrib.auth.decorators import login_required

@login_required
def create_ticket(request):
    """
    Create a new ticket existing one
    """
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            submit = ticket_form.save(commit=False)
            submit.created_by = request.user
            return redirect('profile')
            
    else:
        ticket_form = TicketForm()
    return render(request, 'ticketform.html', {'ticket_form': ticket_form})



# def toggle_status(request, id):



# def make_feature_request(request):
