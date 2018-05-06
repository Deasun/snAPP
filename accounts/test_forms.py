from django.test import TestCase
from django.contrib.auth.models import User
from .forms import *
from .models import Profile


"""
Create Model Instance for Testing
"""
form = UserRegistrationForm({'username': 'Tested', 'email': "tested@mail.com", 'password1': 'q0w9e8r7t7', 'password2': 'q0w9e8r7t7'})

"""
Test UserRegistrationForm
"""
class TestUserRegistrationForm(TestCase):

    """
    Test Registration Form input
    """
    def test_registation_form_input(self):
        self.assertTrue(form.is_valid())
        form_test = form.save()
        self.assertEqual(form_test.username, 'Tested')
        self.assertEqual(form_test.email, 'tested@mail.com')
    
    """
    Testing Duplicate Email Validation Error
    """
    def test_clean_email(self):
        self.assertTrue(form.is_valid())
        form_test = form.save()
        email = form.cleaned_data.get('email')
        form2 = UserRegistrationForm({'username': 'ANOTest', 'email': "tested@mail.com", 'password1': 'Q0w9e8r7t7', 'password2': 'Q0w9e8r7t7'})
        self.assertFalse(form2.is_valid())

        
    """
    Test Non-Matching Password and Validation Error
    """
    def test_matching_passwords(self):
        form_passwords = UserRegistrationForm({'username': 'Tested', 'email': "tested@mail.com", 'password1': 'q0w9e8r7t6', 'password2': 'q0w9e8r7t7' })
        self.assertFalse(form_passwords.is_valid())
        self.assertRaises(ValidationError("Your passwords do not match. Please try again."))
    
    
"""
Test UserEditForm
"""
class TestUserEditForm(TestCase):
    
    """
    Test Valid Blank User Fields
    """
    def test_user_with_blank_field(self):
        form_edit = UserEditForm({'username': 'Tester', 'first_name': '', 'last_name': 'McFester', 'email': ''}) 
        self.assertTrue(form_edit.is_valid())
    
    """
    Test Valid Blank Profile Fields
    """
    def test_profile_with_blank_field(self):
        form_edit = ProfileEditForm({'description': ''})
        self.assertTrue(form_edit.is_valid())

