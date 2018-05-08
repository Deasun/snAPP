from django import forms
from .models import BugTicket

class ReportBugForm(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = ('title', 'description')