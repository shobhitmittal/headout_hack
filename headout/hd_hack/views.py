from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.db.models import Q
from hd_hack import models
from lib import response_handling


import json
import time
import random
import string
import ast
# Create your views here.

@csrf_exempt
def first_page(request):
	if request.method=='POST':
		try:
		#print request.body
			request_rec=ast.literal_eval(request.body)
			#user_name=request_rec['user_id']
			f_name=request_rec['f_name']
			l_name=request_rec['l_name']
			email=request_rec['email']
			if email.lower()=='null':
				email_rand_exist=True
				while email_rand_exist is True:
					email=response_handling.generate_random(10)
					email_rand_exist= models.user_table.objects.filter(email=email).exists()
			else:
				pass
			phone=request_rec['phone']
			if str(phone).lower()=='null':
				phone_rand_exist=True
				while phone_rand_exist is True:
					phone=response_handling.generate_random(10)
					phone_rand_exist= models.user_table.objects.filter(phone=phone).exists()
			else:
				pass
			password=request_rec['password']
		except Exception as err:
			print err
			response_data=response_handling.send_response(iserror=True,error_code=202)
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		email_phone_exists=models.user_table.objects.filter(Q(email=email) | Q(phone=phone)).exists()
		if email_phone_exists is True:
			print 'Duplicate email or phone'
			response_data=response_handling.send_response(iserror=True,error_code=204)
		elif email_phone_exists is False:
			user_iden_found=True
			while user_iden_found is True:
				user_iden=response_handling.generate_random(25)
				user_iden_found=models.user_table.objects.filter(user_iden=user_iden).exists()
			(user_save,user_status)=models.user_table.objects.get_or_create(user_iden=user_iden,defaults={'f_name':f_name,'l_name':l_name,'email':email,'phone':phone,'password':password})
			data={'auth_token':user_iden}
			response_data=response_handling.send_response(data,iserror=False,error_code=200)


			#user_iden=models.CharField(max_length=30,primary_key=True)
			#user_name=models.CharField(max_length=30)
			#f_name=models.CharField(max_length=30)
			#l_name=models.CharField(max_length=30)
			#email=models.CharField(max_length=30)
			#phone=models.CharField(max_length=30)
			#password=models.CharField(max_length=30)

		#user_table
		#send_response(data,iserror=False)
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
		return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def login(request):
	if request.method=='POST':
		print request.body
		request_rec=ast.literal_eval(request.body)
		#user_name=request_rec['user_id']
		user_id=request_rec['user_id']
		password=request_rec['password']
		email_phone_exists=models.user_table.objects.filter(Q(email=user_id) | Q(phone=user_id)).exists()
		if email_phone_exists is True:
			password_db= models.user_table.objects.filter(Q(email=user_id) | Q(phone=user_id)).values('password')
			#DEBUG CODE STARTS
			if len(password_db)>1:
				print 'Something wrong with password as we got 2 password for a single username.'
			#DEBUG CODE ENDS
			if password_db[0]['password'] !=password:
				response_data=response_handling.send_response(iserror=True,error_code=203)
			else:
				user_iden_db= models.user_table.objects.filter(Q(email=user_id) | Q(phone=user_id)).values('user_iden')
				print user_iden_db
				data={'auth_token':user_iden_db[0]['user_iden']}
				response_data=response_handling.send_response(data,iserror=False,error_code=200)
		else:
			print 'Non Existent email or phone'
			response_data=response_handling.send_response(iserror=True,error_code=205)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")		