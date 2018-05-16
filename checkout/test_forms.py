from django.test import TestCase
from django.contrib.auth.models import User
from .forms import PaymentForm, OrderForm
# from .models import Order, OrderLineItem



class TestOrderForm(TestCase):
    def test_successful_order_entry(self):
        form = OrderForm({
            'full_name': 'Test McTester', 
            'phone_number': '07654321213', 
            'country': 'Ireland',  
            'postcode': 'D1', 
            'town_or_city': 'Dublin', 
            'street_address1': '142 Raglan Road',
            'street_address2': 'Lovelyville', 
            'county': 'Dublin',
            })
        self.assertTrue(form.is_valid())    
    
    def test_unsuccessful_order_entry(self):
        form = OrderForm({
            'full_name': '', 
            'phone_number': '07654321213', 
            'country': 'Ireland',  
            'postcode': 'D1', 
            'town_or_city': 'Dublin', 
            'street_address1': '142 Raglan Road',
            'street_address2': 'Lovelyville', 
            'county': 'Dublin',
            })
        self.assertFalse(form.is_valid())    
    
    def test_successful_order_entry_with_blank_field(self):
        form = OrderForm({
            'full_name': 'Test McTester', 
            'phone_number': '07654321213', 
            'country': 'Ireland',  
            'postcode': '', 
            'town_or_city': 'Dublin', 
            'street_address1': '142 Raglan Road',
            'street_address2': 'Lovelyville', 
            'county': 'Dublin',
            })
        self.assertTrue(form.is_valid())
    

class TestPaymentForm(TestCase):
        
    def test_payment_success(self):
        form = OrderForm({
            'credit_card_number': '4242424242424242',  
            'cvv': '424',  
            'expiry_month': '6', 
            'expiry_year': '2019',
            'stripe_id': '',
            })
        self.assertFalse(form.is_valid())