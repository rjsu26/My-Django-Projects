from django.shortcuts import render
from basicApp.forms import UserForm,UserProfileInfoForm
#
from django.urls import reverse  # change to django.url if not working
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'basicApp/index.html')

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form= UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save() #getting form data to database
            user.set_password(user.password) # hashing done
            user.save() #saving the password

            profile = profile_form.save(commit=False) #not saving directly to D.B. to check presemce of profile pic
            profile.user = user #setting the one to one relationship with the User class

            if 'profile_pic' in request.FILES: #use request.FILES to access any kind of file submitted
                profile.profile_pic = request.FILES['profile_pic'] 
            
            profile.save()

            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    
    return render(request,'basicApp/registration.html',
                            {'user_form':user_form,
                                 'profile_form':profile_form,
                                 'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("login failed")
            return HttpResponse("Invalid login details!")
    else:
        return render(request,'basicApp/login.html', {})
