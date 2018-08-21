from django.test import TestCase
from django.test import Client
from .forms import PaymentForm, OrderForm
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import Order
from django.conf import settings
import stripe
from django.utils import timezone
from datetime import datetime


"""
Test Checkout Process
"""

# limited testing as process automated through Stripe's Checkout payment tool
class TestCheckout(TestCase):

    """Simulate login object for accessing checkout"""   
    def setUp(self):
        self.user = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
        self.user.save()
        login = self.client.login(username='Tested', password='q0w9e8r7t7')

    """Test getting checkout page"""    
    def test_checkout(self):
        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout.html") 


        

