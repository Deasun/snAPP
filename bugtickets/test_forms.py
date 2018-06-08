from django.test import TestCase
from .forms import ReportBugForm
from .models import BugTicket

"""
Test UserEditForm
"""
class TestReportBugForm(TestCase):
    
    """Test Incomplete Bug Report"""
    def test_user_with_blank_field(self):
        form_edit = ReportBugForm({'title': 'Tester', 'bug_type': '', 'description': 'This is a test bug report'}) 
        self.assertFalse(form_edit.is_valid())