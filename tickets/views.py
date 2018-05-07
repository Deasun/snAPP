from django.shortcuts import render, redirect, get_object_or_404
from .models import Tickets
from .forms import TicketForm


def create_or_edit_ticket(request):
    """
    Create a new ticket or edit existing one
    """
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect('profile')
    else:
        ticket_form = TicketForm()
    return render(request, 'ticketform.html', {'ticket_form': ticket_form})



# def toggle_status(request, id):



# def make_feature_request(request):
