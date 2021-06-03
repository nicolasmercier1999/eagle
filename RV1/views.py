# -*- coding: utf-8 -*-
'''
Created on 9 déc. 2020

@author: v
'''

from django.shortcuts import render, redirect
from RV1.forms import LoginForm

def welcome(request):
    return render(request, 'welcome.html')

def login(request):

    # If the form has been sent
    if len(request.POST) > 0:
        
        # Instanciation of a LoginForm object
        form = LoginForm(request.POST)
        
        # If inputs are valid
        if form.is_valid():
            return redirect('/welcome')
        
        # If inputs are not valid, return an error
        else:
            return render(request, 'login.html', {'form': form})
            
    # Form wasn't sent
    else:
        # Instanciation of an empty LoginForm object
        form = LoginForm()
        # Refresh the page
        return render(request, 'login.html', {'form': form})
    
    
def home(request):
    return render(request, 'home.html')