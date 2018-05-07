from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from accounts.models import Profile

# Home Page
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')


# Register a User
def registration(request):
    """Redirect logged user to home page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
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
            else:
                messages.error(request, "Unable to register your account at this time. If this problem persists, contact our adminstrator <insert link>")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {"registration_form": registration_form})


# User Login
def login(request):
    """Return a Login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
    
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password = request.POST['password'])
                                    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
    
            else:
                login_form.add_error(None, "Your username or password is incorrect")
        
    else:
        login_form = UserLoginForm()
    
    return render(request, 'login.html', {"login_form": login_form})


@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse('index'))
    

# Edit User Profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form })
    
    