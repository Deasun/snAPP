from django import forms
from .models import BugTicket, Comment

class ReportBugForm(forms.ModelForm):
    class Meta:
        model = BugTicket
        fields = ('title', 'bug_type', 'description')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']