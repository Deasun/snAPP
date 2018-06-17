from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import FeatureTicket
from checkout.models import Order, OrderLineItem
from .forms import RequestFeatureForm, CommentForm


"""
Test FeatureTickets
"""
class TestFeatureticket(TestCase):
    """Simulate login object for accessing featuretickets"""   
    def setUp(self):
        self.user = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
        self.user.save()
        login = self.client.login(username='Tested', password='q0w9e8r7t7')
        ticket = FeatureTicket.objects.create(created_by_id=1, title='TestTitle', feature_type='Convenience', description='This is a test') 

    """Test to get feature request page"""
    def test_request_feature_page(self):
        response = self.client.get("/featuretickets/new/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "request_form.html")
    
    """Test adding feature request"""
    def test_add_feature(self):
        response = self.client.post('/featuretickets/new/', {
        'title': 'Title', 
        'feature_type': 'Design', 
        'description': 'This is a test',
        'created_by_id': '2',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/featuretickets/')
        self.assertEqual(FeatureTicket.objects.count(), 2)
    
    """Test to get add comment page"""
    def test_add_comments_to_feature(self):
        ticket = FeatureTicket.objects.create(created_by_id=1, title='TestTitle', feature_type='Design', description='This is a test') 
        response = self.client.get("/featuretickets/feature/{0}/comment".format(ticket.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_comments_to_feature_form.html")
    
    
    """Test successfully adding comments"""
    def test_add_comments_to_feature_success(self):
        response = self.client.post('/featuretickets/feature/1/comment', {'text': 'this is a comment'})
        self.assertEqual(response.status_code, 302)
    
    """Test for getting feature report"""
    def test_feature_report(self):
        ticket = FeatureTicket.objects.create(created_by_id=1, title='TestTitle', feature_type='Design', description='This is a test') 
        response = self.client.get("/featuretickets/feature/{0}".format(ticket.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "feature_report.html")
    

    """Test for feature_listing status code and template"""
    def test_get_feature_listing(self):
        response = self.client.get(reverse('get_feature_listing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "feature_listing.html")    
    