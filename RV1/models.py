# -*- coding: utf-8 -*-
'''
Created on 9 déc. 2020

@authors: verdier, mercier
'''
from django.db import models

#############################
# Config tables
#############################

class Document_Type(models.Model):
	dct_type = models.CharField(max_length = 50)

class Permission_Type(models.Model):
	prt_name = models.CharField(max_length = 3)

#############################
# Base tables
#############################

class User(models.Model):
    usr_gender = models.BooleanField(default = True) # Female = True / Male = False
    usr_firstname = models.CharField(max_length = 50, default = "")
    usr_lastname = models.CharField(max_length = 50, default = "")
    usr_email = models.CharField(max_length = 100, default = "")
    usr_active = models.BooleanField(default = True)
    usr_root_dir = models.CharField(max_length = 100, default = "/.tempRootDir")

class Classroom(models.Model):
	cls_name = models.CharField(max_length = 6)
	cls_capacity = models.IntegerField()

class Module(models.Model):
	mdl_name = models.CharField(max_length = 50)
	mdl_start_date = models.DateField()
	mdl_end_date = models.DateField()

class Chapter(models.Model):
	mdl_id = models.ForeignKey(Module, on_delete = models.CASCADE) 
	chp_title = models.CharField(max_length = 50)

class Course(models.Model):
	mdl_id = models.ForeignKey(Module, on_delete = models.CASCADE) 
	chp_id = models.ForeignKey(Chapter, on_delete = models.CASCADE)
	crs_name = models.CharField(max_length = 50)
	crs_start_datetime = models.DateTimeField()
	crs_end_datetime = models.DateTimeField()
	crs_classroom = models.ManyToManyField(Classroom, related_name = 'classroom_attributed')
	crs_teacher = models.ManyToManyField(User, related_name = "teacher_participating")

class Document(models.Model):
	dcm_name = models.CharField(max_length = 100)
	dcm_subpath = models.CharField(max_length = 200)
	dct_id = models.ForeignKey(Document_Type, on_delete = models.CASCADE)
	usr_owner = models.ForeignKey(User, on_delete = models.CASCADE)

class Group(models.Model):
	grp_code = models.CharField(max_length = 10)
	grp_name = models.CharField(max_length = 50)
	grp_start_date = models.DateField()
	grp_end_date = models.DateField()
	grp_course = models.ManyToManyField(Module, related_name = 'course_taken')
	grp_user = models.ManyToManyField(User, related_name = 'user_belonging')

#############################
# Many-to-Many tables
#############################

class Share_File(models.Model):
	dcm_id = models.ForeignKey(Document, on_delete = models.CASCADE)
	usr_id = models.ForeignKey(User, on_delete = models.CASCADE)
	prt_id = models.ForeignKey(Permission_Type, on_delete = models.CASCADE)

class Share_Support(models.Model):
	dcm_id = models.ForeignKey(Document, on_delete = models.CASCADE)
	mdl_id = models.ForeignKey(Module, on_delete = models.CASCADE) 
	chp_id = models.ForeignKey(Chapter, on_delete = models.CASCADE)
	crs_id = models.ForeignKey(Course, on_delete = models.CASCADE)
