from django import forms
from .models import BugTicket, RequestTicket

class ReportBugForm(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = ('ticket', 'title', 'description')

class RequestFeatureForm(forms.ModelForm):
    class Meta:
        model = RequestTicket
        fields = ('ticket', 'title', 'description', 'contribution')