# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.template.loader import get_template
from django.http import HttpResponse
from .models import News
# Create your views here.

def home(request):
	context = locals()
	template = 'post.html'
	posts = News.objects.all()
	return render(request,template,{'news':posts})

