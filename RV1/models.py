# -*- coding: utf-8 -*-
'''
Created on 9 déc. 2020

@author: v
'''
from django.db import models

class User(models.Model):
    gender = models.IntegerField()
    lastname = models.CharField(max_length=40)
    firstname = models.CharField(max_length=40)
    birthdate = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=40)