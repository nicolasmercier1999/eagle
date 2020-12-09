# -*- coding: utf-8 -*-
'''
Created on 9 déc. 2020

@author: v
'''
# Import the forms library
from django import forms

# Declaration of LoginForm class that inherits from Form class
class LoginForm(forms.Form):
    # This form has two fields, email and password
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget = forms.PasswordInput)
    
    def clean(self):
        # Call the function from the parent class
        cleaned_data = super(LoginForm, self).clean()
        
        # Get the values of the fields
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        
        # Check the values' validity
        if email and password:
            if email != 'admin@gmail.com' or password != 'admin':
                raise forms.ValidationError("Email or password is incorrect")
        
        return cleaned_data
        