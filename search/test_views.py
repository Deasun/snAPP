from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
from checkout.models import Order, OrderLineItem
from featuretickets.models import FeatureTicket
from bugtickets.models import BugTicket


"""
Test Search
"""
class TestSearch(TestCase):
    """
    Simulate login object for accessing featuretickets
    """   
    def setUp(self):
        self.user = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
        self.user.save()
        login = self.client.login(username='Tested', password='q0w9e8r7t7')
    
    
    """
    Test feature search status code and page render
    """
    def test_feature_search(self):
        response = self.client.get("/search/feature/?q={0}".format("bug"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "feature_listing.html")    
    
    """
    Test bug search status code and page render
    """
    def test_bug_search(self):
        response = self.client.get("/search/bug/?q={0}".format("bug"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug_listing.html")