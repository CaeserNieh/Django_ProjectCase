# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class News(models.Model):
	title = models.CharField(max_length = 200)
	content = RichTextUploadingField(null=True,blank=True)
	group = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.title
