from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
from bugtickets.models import BugTicket
from bugtickets.forms import ReportBugForm


"""
Test BugTickets
"""
class TestBugticket(TestCase):

    """Simualte login users and bugticket"""
    def setUp(self):    
        self.userA = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
        self.userB = User.objects.create_user('Tested2', 'tested2@mail.com', 'q0w9e8r8t8')
        self.userA.save()
        self.userB.save()
        login = self.client.login(username='Tested', password='q0w9e8r7t7')
        ticket = BugTicket.objects.create(created_by_id=1, title='TestTitle', bug_type='Syntax', description='This is a test') 

    """Test getting bug report page"""
    def test_report_bug_redirect(self):
        response = self.client.get("/bugtickets/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "report_form.html") 
    
    """Test valid ReportBugForm submission"""
    def test_report_bug(self):
        response = self.client.post('/bugtickets/new/', {
            'title': 'Title', 
            'bug_type': 'Syntax', 
            'description': 'This is a test',
            'created_by_id': '2',
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/bugtickets/')
        self.assertEqual(BugTicket.objects.count(), 2)
        
    """Test Bug Upvote"""        
    def test_upvote_bug(self):
        response = self.client.post('/bugtickets/upvote/1')
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)

    """Test getting add comment to bug page"""
    def test_add_comments_to_bug(self):
        response = self.client.get("/bugtickets/bug/1/comment")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_comments_to_bug_form.html") 
    
    """Test successfully adding comments"""
    def test_add_comments_to_bug_success(self):
        response = self.client.post('/bugtickets/bug/1/comment', {'text': 'this is a comment'})
        self.assertEqual(response.status_code, 302)

    """Test for bug_listing status code and template"""
    def test_get_bug_listing(self):
        response = self.client.get(reverse('get_bug_listing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug_listing.html")    

    """Test for getting bug_report"""
    def test_bug_report(self):
        response = self.client.get("/bugtickets/bug/1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug_report.html")
    
    """Test no bug exists"""
    def test_report_bug_not_exist(self):
        response = self.client.get("/bugtickets/bug/3")
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "There is no bug with that identity. Please search again.")
        
        
        
        
        