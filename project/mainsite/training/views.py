# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.

def trainingboss(request):
	template = get_template('training_boss.html')
	html = template.render(locals())
	return HttpResponse(html)

def trainingdealer(request):
	template = get_template('training_dealer.html')
	html = template.render(locals())
	return HttpResponse(html)