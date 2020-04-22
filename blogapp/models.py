from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime

def valid_image(value):
	import os
	from django.core.exceptions import ValidationError
	format=os.path.splitext(value.name)[1]
	valid_format=['.png' , '.jpg']
	if format.lower() not in valid_format:
		raise ValidationError('not support format')


class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	avatar=models.FileField(upload_to='files/avatar/',blank=False,null=False,validators=[valid_image])
	description=models.CharField(max_length=512,blank=False,null=False)

class article(models.Model):
	title=models.CharField(max_length=50 , blank=False , null=False)
	cover=models.FileField(upload_to='files/cover_article/', blank=False, null=False,validators=[valid_image])
	content=RichTextField()
	date=models.DateTimeField(default=datetime.now(),blank=False)
	category=models.ForeignKey('category',on_delete=models.CASCADE)
	authoe=models.OneToOneField(UserProfile,on_delete=models.CASCADE)

class category (models.Model):
	title=models.CharField(max_length=50, blank=False,null=False)
	cover=models.FileField(upload_to='files/cover_category/',blank=False , null=False,validators=[valid_image])

