from multiprocessing import context
import profile
from django.shortcuts import render, redirect
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.forms import EditProfileForm
from weddings.views import weddings
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, SkillForm
# from .utils import searchProject


# Create your views here.
def logOutUser(request):
    logout(request)
    messages.info(request, "user was logged out ")
    return redirect('login')

def profileUpdate(sender, instance, created, **kwargs):

    print("Profile Saved")

    print("Instance:", instance)

    print("CREATED:", created)

    post_save.connect(profileUpdate, sender=Profile)

def profiles(request):
    profiles = Profile.objects.all()

    context = {

        'profiles': profiles        
    }
    return render (request, 'users/profiles.html',context)

def userprofile(request, pk):

    profile = Profile.objects.get(id=pk)

    skills= profile.skill_set.exclude(description__exact="")

    others = profile.skill_set.filter(description="")

    context={

    'profile':profile,

    'skills':skills,

    'others':others
    }

    return render(request, "users/profile.html", context)
def registerUser(request):
    form = UserRegisterForm()
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower() 
            user.save()
            messages.success(request, "User account was created succesfully")
            login(request, user) #Login the user automatically
            return redirect('profiles') #Redirect to the profiles page

    context={
          'form':form
    }
    return render(request,'users/registration.html', context )

    

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
  
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "username does not exist")

            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
            
        else:
            messages.error(request, "username or password is incorrect")

    return render (request, 'users/login.html')

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    weddings = profile.wedding_set.all()
    skills = profile.skill_set.all
    context={
        'profile':profile,
        'skills':skills,
        'weddings':weddings

    }
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    form = EditProfileForm()
    context = {
         'form':form
    }
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {
        'messageRequests':messageRequests,
        'unreadCount':unreadCount
    }
    return render(request, 'users/inbox.html', context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method=='POST':
        form = SkillForm(request.POST)
        if form.is_valid:
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account') 

    context={
        'form':form
    }
    return render(request, 'users/skill_form.html', context)







