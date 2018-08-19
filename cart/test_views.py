from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
from featuretickets.models import FeatureTicket


"""
Test Cart
"""
class TestCart(TestCase):
    """Simulate login object for accessing bugtickets"""   
    def setUp(self):
        self.user = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
        self.user.save()
        login = self.client.login(username='Tested', password='q0w9e8r7t7')
    
    """Test getting cart page"""
    def test_view_cart(self):    
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html") 
    
    """Test adding items to cart"""
    def test_add_to_cart(self):
        ticket = FeatureTicket.objects.create(created_by_id=1, title='TestTitle', feature_type='Design', description='This is a test') 
        response = self.client.post('/cart/add/1', {'quantity': '2'})
        self.assertEqual(response.status_code, 302)
    
    """Test adjust amount of items in cart"""
    def test_adjust_cart(self):
        ticket = FeatureTicket.objects.create(created_by_id=1, title='TestTitle', feature_type='Design', description='This is a test') 
        response = self.client.post('/cart/add/1', {'quantity': '2'})
        response = self.client.post('/cart/adjust/1', {'quantity': '3'})