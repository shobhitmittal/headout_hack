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
	created_at=models.CharField(max_length=30)
	updated_at=models.CharField(max_length=30)

class event_table(models.Model):
	event_id= models.CharField(max_length=200,primary_key=True)
	event_name=models.CharField(max_length=200)
	event_desc=models.TextField()
	event_location=models.CharField(max_length=200)
	created_by= models.ForeignKey(user_table,related_name='creator')
	updated_by=models.ForeignKey(user_table,related_name='updator')
	#event_members=
	#event_admins=
	#event_participate=
	#event_maybe=
	#event_coming=
	#event_participated=
	event_start_date=models.CharField(max_length=200)
	event_end_date=models.CharField(max_length=200)
	#AUTO
	event_created_at=models.CharField(max_length=200)
	event_updated_at=models.CharField(max_length=200)

class user_location(models.Model):
	user_iden=models.ForeignKey(user_table)
	current_location=models.CharField(max_length=200)
	last_updated=models.CharField(max_length=100)