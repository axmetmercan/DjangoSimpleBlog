from django.shortcuts import render,redirect
from django.urls.conf import path
from . forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.


def register(request):
    
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')

            new_user = User(username = user_name)
            new_user.set_password(password)
            new_user.save()

            login(request,new_user)

            messages.success(request, 'Succesfully signed in...')

            return redirect('index')
        context = {
            'form' : form,
        }
        return render(request, 'register.html', context)


    
def loginUser(request):

    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, 'There is no such user ')
            return render(request, 'login.html', context)

        messages.success(request, 'Succesfully Logged in')
        login(request, user)
        return redirect('index')

    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been signed out')
    return redirect('index')