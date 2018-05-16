from django.test import TestCase
from .forms import ReportBugForm
from .models import BugTicket

"""
Test UserEditForm
"""
class TestReportBugForm(TestCase):
    
    """
    Test Valid Blank User Fields
    """
    def test_user_with_blank_field(self):
        form_edit = ReportBugForm({'title': 'Tester', 'description': 'This is a test bug report'}) 
        self.assertTrue(form_edit.is_valid())