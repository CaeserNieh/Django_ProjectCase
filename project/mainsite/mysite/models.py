# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserProfile(models.Model):
	chinese_name = models.CharField(max_length=200)
	english_name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	gender = models.CharField(max_length=20,default='Female')
	birth = models.CharField(max_length=200)
	password1 = models.CharField(max_length=500)
	password2 = models.CharField(max_length=500)
	email = models.EmailField(max_length=200,default="xxx@gmail.com")
	number = models.CharField(max_length=200)
	home_number = models.CharField(max_length=200,default='0987xxooox')
	address = models.CharField(max_length=200,default='your home address')
	def __unicode__(self):
		return self.username