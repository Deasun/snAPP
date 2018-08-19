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

    """Testing Stripe Payment Form"""
    def test_card_rejection_no_js_stripe_payment_form(self):
        
        stripe.api_key = settings.STRIPE_SECRET
        token = stripe.Token.create(
            card={
                'number': '4242424242424242',
                'exp_month': '6',
                'exp_year': str(datetime.today().year + 1),
                'cvc': '123',
            })
        response = self.client.post('/checkout/', 
            data={
                'full_name': 'Robert McCann',
                'street_address1': '376 Rue Street', 
                'street_address2': 'Percyville',
                'town_or_city': 'Inis glas',
                'county': 'Aontriom',
                'postcode': 'BT54 TC4',
                'country': 'Eire',
                'phone_number': '0712345678',
                'date': '21-03-2018',
                'stripeToken': token.id,
            })
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "We were unable to take a payment with that card.")
        
