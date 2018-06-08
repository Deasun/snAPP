from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import Profile
from bugtickets.models import BugTicket
from bugtickets.forms import ReportBugForm



"""
Test BugTickets
"""
class TestBugticket(TestCase):
    
# Passing but not registering on Coverage
    """Test valid ReportBugForm"""
    def test_report_bug(self):
        report_form = ReportBugForm({
            'title': 'TestTitle', 
            'bug_type': 'Syntax', 
            'description': 'This is a test',
            'created_by': 'TestTim'
        })
        self.assertEquals(report_form.is_valid(), True)

# Passing but not registering on Coverage
    """Test redirect following bug report form submission"""
    def test_report_bug_redirect(self):    
        page = self.client.post("/bugtickets/new/")
        self.assertEqual(page.status_code, 302)
    

        
        
        
        
        