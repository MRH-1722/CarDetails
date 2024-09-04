from django.shortcuts import render , redirect 
from .models import Profile
from projects.models import Detail
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm , ProfileForm

# Create your views here.

def loginUser(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user =  authenticate(request, username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'Username OR password is incorrect')
        
    return render(request , 'login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request,'User successfully logout')
    return redirect('login_register')

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
            return redirect('profiles')
        
        else:
            messages.error(request, 'An error has occured during registration.')

    context = {'page':page , 'form':form}
    return render(request , 'login_register.html' , context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles' : profiles}
    return render(request , 'profiles.html' , context)  

def userProfile(request, pk):
    
    profile = Profile.objects.get(uuid=pk)
    topSkills = profile.skill_set.exclude(description__exact = '')
    otherSkills = profile.skill_set.filter(description = '')
    context = {'profile' : profile, 'topSkills':topSkills, 'otherSkills':otherSkills }
    return render(request , 'user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    details = profile.detail_set.all()
    context = {'profile':profile , 'skills': skills, 'details' : details}
    return render(request, 'account.html', context)

@login_required(login_url='login')
def editAccount(request):
    form = ProfileForm()
    context = {'form' : form}
    return render(request, 'profile-form.html' , context)