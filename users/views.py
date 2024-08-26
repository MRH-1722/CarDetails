from django.shortcuts import render
from .models import Profile
from projects.models import Detail

# Create your views here.

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