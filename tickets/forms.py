from django import forms
from .models import Tickets

class ReportBugForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('ticket', 'title', 'description', 'status')

class RequestFeatureForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('ticket', 'title', 'description', 'contribution', 'status')