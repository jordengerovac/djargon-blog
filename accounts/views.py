# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Logging in
            user = form.save()
            login(request, user)
            return redirect('entries:all')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Logging in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('entries:all')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('entries:all')