from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.core.urlresolvers import reverse
from courbe_de_charge.models import UsersLP

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login_auth(request, user)
            return redirect('accueil')
    else:
        form = RegisterForm()
    return render(request, 'accueil/signup.html', {'form': form})

def login(request):
    error = False
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try :
                username = User.objects.get(email=email).username
                user = authenticate(username=username, password=password)
                login_auth(request, user)
                return redirect('accueil')
            except :
                error = True
    else:
        form = LoginForm()
    return render(request, 'accueil/login.html', locals())

def home(request) :
    user_result = True
    
    if request.user.is_authenticated :
        email = request.user.email
        try :
            userLP = UsersLP.objects.get(user = email)
        except :
            user_result = False
        
    return render(request, 'accueil/home.html', {'user_result' : user_result})

def logout(request):
    logout_auth(request)
    return redirect('accueil')
