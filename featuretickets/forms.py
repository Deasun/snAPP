from django import forms
from .models import FeatureTicket, Comment

class RequestFeatureForm(forms.ModelForm):
    class Meta:
        model = FeatureTicket
        fields = ('title', 'description', 'links', 'contribution')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']