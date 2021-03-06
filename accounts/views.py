from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from accounts.models import Profile
from bugtickets.models import BugTicket
from featuretickets.models import FeatureTicket
from context_processors import get_random_alert
from datetime import date, datetime



"""
Home Page
"""
def index(request):
    """Return the home page"""
    if request.user.is_authenticated:
        return redirect('profile', id=request.user.id)
    
    return render(request, 'index.html')


def registration(request):
    """
    Register a User
    """
    
    """Redirect logged user to profile page"""
    if request.user.is_authenticated:
        return redirect('profile', id=request.user.id)

    elif request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            # Create instance of Profile model in OneToOne relationship with User Model
            Profile.objects.create(user=user)
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You're registered. Welcome to snAPP!")
                return redirect('profile', id=request.user.id)
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {"registration_form": registration_form})


def login(request):
    """
    User Login
    """
    
    """Access login page and enter credentials"""
    if request.user.is_authenticated:
        return redirect('profile', id=request.user.id)
        
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
    
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password = request.POST['password'])
                                    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect('profile', id=request.user.id)
            else:
                login_form.add_error(None, "Your username or password is incorrect")
        
    else:
        login_form = UserLoginForm()
    
    return render(request, 'login.html', {"login_form": login_form})


@login_required
def user_profile(request, id):
    """
    User Profile Page
    """
    
    """The user's profile page"""
    user = get_object_or_404(User, id=id)
    auth_user = request.user
    bugs = BugTicket.objects.filter(created_by=id)
    features = FeatureTicket.objects.filter(created_by=id)
    
    # filter out expired alerts
    today = datetime.today()
    alerts = Profile.objects.filter(alert_date__gte=today)
    
    return render(request, 'profile.html', {
                "features": features, 
                "bugs": bugs, 
                "user": user, 
                "auth_user": auth_user, 
                "alerts": alerts,
                })


@login_required
def logout(request):
    """
    Logout
    """
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse('index'))
    

@login_required
def edit_profile(request):
    """
    Edit User Profile
    """
    """edit both the user and profile model instances"""
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        
        return redirect('profile', id=request.user.id)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form })

@login_required
def delete_profile(request, id):
    """
    Delete user profile
    """
    if request.method == 'POST':
        Profile.objects.filter(user=request.user).delete()
        user = get_object_or_404(User, id=id)
        user.delete()
        messages.success(request, "You have left the snAPP network. Thank you for your contribution.")
        return redirect(reverse('index'))
                
    
    