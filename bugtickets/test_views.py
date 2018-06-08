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
    
    """
    Simualte login object for accessing bugtickets
    """   
    def setUp(self):
        self.user = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
        self.user.save()
        login = self.client.login(username='Tested', password='q0w9e8r7t7')

    """
    Test getting bug report page
    """
    def test_report_bug_redirect(self):    
        response = self.client.get("/bugtickets/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "report_form.html") 


############################## Passing but not registering on Coverage
    """
    Test valid ReportBugForm submission
    """
    def test_report_bug(self):
        report_form = ReportBugForm({
            'title': 'TestTitle', 
            'bug_type': 'Syntax', 
            'description': 'This is a test',
        })
        self.assertEquals(report_form.is_valid(), True)
        # submit = report_form.save(commit=False) 
        # submit.created_by = self.user 
        # submit.save()
######################################### 

    """
    Test Bug Upvote
    """
    def test_upvote_bug(self):
        pass
        # response = self.client.post("/add", {"name": "Create a Test"})
        # item = get_object_or_404(Item, pk=1)
        # self.assertEqual(item.done, False)
    

# Might not end up using this function
    """
    Test Edit Bug
    """
    def test_edit_bug(self):
        pass
    
    
    """
    Test Delete Bug
    """
    def test_delete_bug(self):
        pass

    
    """
    Test getting add comment to bug page
    """
    def test_add_comments_to_bug(self):
        ticket = BugTicket.objects.create(created_by_id=1, title='TestTitle', bug_type='Syntax', description='This is a test') 
        response = self.client.get("/bugtickets/bug/{0}/comment".format(ticket.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_comments_to_bug_form.html") 
    
    
    """
    Test successfully adding comments
    """
    def test_add_comments_to_bug_success(self):
        pass
    
    
    """
    Test for bug_listing status code and template
    """
    def test_get_bug_listing(self):
        response = self.client.get(reverse('get_bug_listing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug_listing.html")    


# Need to figure out a reverse match here 
    """
    Test for getting bug_report
    """
    def test_bug_report(self):
        ticket = BugTicket.objects.create(created_by_id=1, title='TestTitle', bug_type='Syntax', description='This is a test') 
        response = self.client.get("/bugtickets/bug/{0}".format(ticket.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug_report.html")
        
        
        
        
        
        