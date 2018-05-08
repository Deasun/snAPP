from django import forms
from .models import FeatureTicket

class RequestFeatureForm(forms.ModelForm):
    class Meta:
        model = FeatureTicket
        fields = ('title', 'description', 'links', 'contribution')