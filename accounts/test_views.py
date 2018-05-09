from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Profile
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.messages import get_messages



"""
Test User registration
"""
class TestUserRegistration(TestCase):
    
    """Test that registration produces model instant and success message"""
    def test_registration_successful(self):
        response = self.client.post(reverse('registration'),
                        data={'username': 'Tested', 
                                'email': "tested@mail.com", 
                                'password1': 'q0w9e8r7t7', 
                                'password2': 'q0w9e8r7t7'})
        self.assertEqual(Profile.objects.count(), 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You're registered. Welcome to snAPP!")
        self.assertTemplateUsed(response, "registration.html")
        

        
    
"""
Test Login
"""
class TestLogin(TestCase):
    
    """Test Login Page render"""
    def test_login_page_render(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


"""
Test logged user destination & templates
"""
class TestLoggedViews(TestCase):
    
    """Set up class for logged in user"""
    
    def setUp(self):
        self.user = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
        self.user.save()
        login = self.client.login(username='Tested', password='q0w9e8r7t7')
        
    
    """Logged in user access home page"""
    
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    """Logged in user redirected from login page"""
    
    def test_redirect_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/')
    
    """Logged in user redirected from registration page"""
    
    def test_redirect_register_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/')

    """Logged in user access profile page"""
    
    def test_get_profile_page_redirect(self):
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    """Logged in user successful logout"""
    
    def test_get_logout_redirect(self):
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have been successfully logged out!')


"""
Test Non-logged user destination & templates
"""
class TestNonLoggedViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    

    
