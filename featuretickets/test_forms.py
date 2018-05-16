from django.test import TestCase
from .forms import RequestFeatureForm, CommentForm

"""
Test RequestFeatureForm
"""
class TestRequestFeatureForm(TestCase):
    
    """
    Test Valid Form Completion
    """
    def test_completed_form(self):
        form = RequestFeatureForm({'title': 'Tester', 'description': 'This is a test feature request'}) 
        self.assertTrue(form.is_valid())

class TestCommentForm(TestCase):
    """
    Test Invalid Form Completion
    """
    def test_invalid_form_completion(self):
        form = CommentForm({'text': ''})
        self.assertFalse(form.is_valid())
        