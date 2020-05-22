from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
from .forms import RegisterationForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse



def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password, email=email)
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = RegisterationForm()
    return render(request, 'users/registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('myrestaurants:restaurant_list'))
            else:
                return render(request, 'users/login.html', {'form': form, 'message': 'Wrong password. Please try again.'})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('myrestaurants:restaurant_list'))