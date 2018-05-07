from django import forms
from .models import Tickets
from .choices import ticket_type

class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('ticket', 'title', 'description',)