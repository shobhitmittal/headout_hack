from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user_table(models.Model):
	user_iden=models.CharField(max_length=30,primary_key=True)
	#user_name=models.CharField(max_length=30)
	f_name=models.CharField(max_length=30,null=True)
	l_name=models.CharField(max_length=30,null=True)
	email=models.CharField(max_length=30,unique=True,null=True)
	phone=models.CharField(max_length=30,unique=True,null=True)
	password=models.CharField(max_length=30)