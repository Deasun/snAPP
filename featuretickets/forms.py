from django import forms
from .models import FeatureTicket, Comment

class RequestFeatureForm(forms.ModelForm):
    class Meta:
        model = FeatureTicket
        fields = ['title', 'feature_type', 'description', 'links']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']