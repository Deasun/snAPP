from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Registration
class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""
    
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput)
    
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'This email address is currently registered to another snAPP member.')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Your passwords do not match. Please try again.")
        
        return password2

# Login
class UserLoginForm(forms.Form):
    """Forms to be used to log users in"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Edit User Profile - provide more details than asked for a registration
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        fields = ('image', 'trade_union', 'description', 'alert', 'alert_date')
        labels = {
            'image': _('Profile Image'),
            'trade_union': _('Trade Union'),
            'description': _('Brief description of yourself'),
            'alert': _('Update your snAPP Alert'),
            'alert_date': _('Enter what date your Alert ends'),
        }
        