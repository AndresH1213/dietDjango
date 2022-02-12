from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, ProfileForm


# Create your views here.
def homePage(request):
    return render(request,'users/home.html')

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = get_user_model().objects.get(username=username)
        except:
            messages.error(request, f"Username ${username} doesn't exist")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
    
    return render(request, 'users/login-register.html')
    

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('profile-information')
        else:
            messages.error(request, "Can't register the account, please check the fields")
    
    context = {'page': page, 'form': form}

    return render(request, 'users/login-register.html', context)

@login_required(login_url='login')
def profile(request):
    return render(request, 'users/profile.html')

@login_required(login_url='login')
def editProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        
        if form.is_valid():
            form.save()

            return redirect('profile')
    
    return render(request, 'users/profile-form.html', {'form': form})