from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader, Context
from django.db.models import Q
from django.db.models import Count
from hd_hack import models
from lib import response_handling
from lib import encrypting_hashing

from lib import send_gcm_message

import sys
import traceback
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
			##print type(request.POST['data']),request.POST
			#print 25,request.POST['data']
			print request.body
			request_rec=ast.literal_eval(request.body)
			isemail=True
			##request_rec=json.loads(request.POST['data'])
			#print type(request_rec)
			#print 27,ast.literal_eval(request_rec)
			##print 28,json.loads(request_rec)
			#user_name=request_rec['user_id']
			f_name=request_rec['f_name']
			l_name=request_rec['l_name']
			email=request_rec['email']
			if email.lower()=='null':
				isemail=False
				email_rand_exist=True
				while email_rand_exist is True:
					email=response_handling.generate_random(10)
					email=encrypting_hashing.hashing(email,str(time.time()))
					email_rand_exist= models.user_table.objects.filter(email=email).exists()
			else:
				pass
			phone=request_rec['phone']
			if str(phone).lower()=='null':
				isemail=True
				phone_rand_exist=True
				while phone_rand_exist is True:
					phone=response_handling.generate_random(10)
					phone=encrypting_hashing.hashing(phone,str(time.time()))					
					phone_rand_exist= models.user_table.objects.filter(phone=phone).exists()
			else:
				pass
			password=request_rec['password']
			isadmin=request_rec['isadmin']
			under_admin=request_rec['under_admin']
			if under_admin is None:
				under_admin='None'
		except Exception as err:
			print 46,err
			print traceback.print_exc(file=sys.stdout)
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
				if isemail is True:
					user_iden=encrypting_hashing.hashing(email,user_iden)
				else:
					user_iden=encrypting_hashing.hashing(phone,user_iden)					
				user_iden_found=models.user_table.objects.filter(user_iden=user_iden).exists()
			created_at=int(time.time())
			(user_save,user_status)=models.user_table.objects.get_or_create(user_iden=user_iden,defaults={'f_name':f_name,'l_name':l_name,'email':email,'phone':phone,'password':password,'created_at':created_at,'updated_at':created_at,'isadmin':isadmin,'under_admin':under_admin})
			print (user_save,user_status)
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
		print request.POST
		print request.body
		request_rec=ast.literal_eval(request.body)
		#request_rec=json.loads(request.POST['data'])
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
				#DEBUG CODE STARTS
				if len(user_iden_db)>1:
					print 'Something wrong with password as we got 2 password for a single username.'
				#DEBUG CODE ENDS
				data={'auth_token':user_iden_db[0]['user_iden']}
				response_data=response_handling.send_response(data,iserror=False,error_code=200)
		else:
			print 'Non Existent email or phone'
			response_data=response_handling.send_response(iserror=True,error_code=205)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def create_event(request):
	if request.method=='POST':
		print request.POST
		#print request.body
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		if api_key is True:
			#request_rec=json.loads(request.POST['data'])
			user_iden=request_rec['auth_token']
			event_id=request_rec['event_id']
			event_name=request_rec['event_name']
			event_desc=request_rec['event_desc']
			event_location=request_rec['event_location']
			created_by=request_rec['created_by']
			updated_by=request_rec['updated_by']
			event_start_date=request_rec['event_start_date']
			event_end_date=request_rec['event_end_date']
			event_created_at=request_rec['event_created_at']
			event_updated_at=request_rec['event_updated_at']
			event_id_found=True
			while event_id_found is True:
				event_id=response_handling.generate_random(25)
				event_id=encrypting_hashing.hashing(user_iden,event_id)
				event_id_found=models.event_table.objects.filter(event_id=event_id).exists()
			event_created_at=int(time.time())
			(event_save,event_status)=models.event_table.objects.get_or_create(event_id=event_id,defaults={'event_name':event_name,'event_desc':event_desc,'event_location':event_location,'created_by':created_by,'updated_by':updated_by,'event_start_date':event_start_date,'event_end_date':event_end_date,'event_created_at':event_created_at,'event_updated_at':event_created_at})
			print (event_save,event_status)
			user_iden_obj=models.user_table.objects.get(user_iden=user_iden)
			event_id_obj=models.event_table.objects.get(event_id=event_id)		
			admin_status=models.event_member.objects.create(event_id=event_id_obj,user_iden=user_iden_obj,admin=True,event_gng=True,event_maybe=False,event_nt_gng=False,event_participated=False)
			print admin_status
			if event_status is True:
				data={'event_id':event_id}
				response_data=response_handling.send_response(data,iserror=False,error_code=200)
			else:
				response_data=response_handling.send_response(iserror=True,error_code=207)
			#event_id= models.CharField(max_length=200,primary_key=True)
			#event_name=models.CharField(max_length=200)
			#event_desc=models.TextField()
			#event_location=models.CharField(max_length=200)
			#created_by= models.ForeignKey(user_table,related_name='creator')
			#updated_by=models.ForeignKey(user_table,related_name='updator')
			##event_members=
			##event_admins=
			##event_participate=
			##event_maybe=
			##event_coming=
			##event_participated=
			#event_start_date=models.CharField(max_length=200)
			#event_end_date=models.CharField(max_length=200)
			##AUTO
			#event_created_at=models.CharField(max_length=200)
			#event_updated_at=models.CharField(max_length=200)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def user_loc_update(request):
	if request.method=='POST':
		print request.POST
		print request.body
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		if api_key is True:
			#request_rec=json.loads(request.POST['data'])
			user_iden=request_rec['user_id']
			current_location=request_rec['cur_loc']
			last_updated=int(time.time())
			#user_iden=models.ForeignKey(user_table)
			#current_location=models.CharField(max_length=200)
			#last_updated=models.CharField(max_length=100)
			user_iden_obj=models.user_table.objects.get(user_iden=user_iden)
			user_loc_status=models.user_location.objects.create(user_iden=user_iden_obj, current_location=current_location,last_updated=last_updated)
			#(location_save,location_status)=models.user_location.objects.get_or_create(user_iden=user_iden,defaults={'event_name':event_name,'event_desc':event_desc,'event_location':event_location,'created_by':created_by,'updated_by':updated_by,'event_start_date':event_start_date,'event_end_date':event_end_date,'event_created_at':event_created_at,'event_updated_at':event_created_at})
			print user_loc_status
			data={'data':'Location_save_suceess'}
			response_data=response_handling.send_response(data,iserror=False,error_code=200)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)	
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def invite_members(request):
	if request.method=='POST':
		print request.POST
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		if api_key is True:
			#request_rec=json.loads(request.POST['data'])
			datas=request_rec['data']
			data_return={}
			data_return_nt_fnd=[]
			phone_list=[]
			email_list=[]
			for data in datas:
				if data.isdigit() is True:
					phone_list.append(data)
					data_email_user_iden=models.user_table.objects.values('user_iden').filter(under_admin=request_rec['auth_token']).get(phone=data)
					if data_email_user_iden[0]['user_iden']:
						data_return[data]=data_email_user_iden[0]['user_iden']
					else:
						data_return_nt_fnd.append(data)
				else:
					email_list.append(data)
					data_phone_user_iden=models.user_table.objects.values('user_iden').filter(under_admin=request_rec['auth_token']).get(email=data)
					if data_phone_user_iden[0]['user_iden']:
						data_return[data]=data_phone_user_iden[0]['user_iden']
					else:
						data_return_nt_fnd.append(data)
			data={'email_phone_user_id':data_return,'user_not_found':data_return_nt_fnd}
			response_data=response_handling.send_response(data,iserror=False,error_code=200)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)	
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def gcm_inbound(request):
	if request.method=='POST':
		print request.POST
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		if api_key is True:
			#request_rec=json.loads(request.POST['data'])
			gcm_id=request_rec['gcm_id']
			user_iden=request_rec['user_id']
			created_at=int(time.time())
			user_iden_obj=models.user_table.objects.get(user_iden=user_iden)
			(gcm_save,gcm_status)=models.gcm_table.objects.get_or_create(gcm_id=gcm_id,defaults={'user_iden':user,'created_at':created_at})
			print (gcm_save,gcm_status)
			if gcm_status is True:
				data={'gcm_id':gcm_id}
				response_data=response_handling.send_response(data,iserror=False,error_code=200)
			else:
				response_data=response_handling.send_response(iserror=True,error_code=207)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def gcm_outbound_message(request):
	if request.method=='POST':
		print request.POST
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		message=request_rec['message']
		user_id_list=request_rec['user_id_list']
		if api_key is True:
			user_id_list=models.gcm_table.objects.values_list('gcm_id').filter(user_iden__in=user_id_list)
			status_gcm_send=send_gcm_message.send_message_gcm(user_id_list,message)
			if status_gcm_send is True:
				data={'user_id_list':user_id_list}
				response_data=response_handling.send_response(data,iserror=False,error_code=200)
			else:
				response_data=response_handling.send_response(not_found=True,error_code=209)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")



@csrf_exempt
def send_location(request):
	if request.method=='POST':
		print request.POST
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		if api_key is True:
			#request_rec=json.loads(request.POST['data'])
			event_id=request_rec['event_id']
			user_iden_req=request_rec['user_id']
			user_iden_list=request_rec['user_id_share']
			data_return={}
			under_admin_users=models.user_table.objects.values('under_admin').filter(isadmin=user_iden_req)
			list_user_under_admin=[]
			list_user_not_under_admin=[]
			for under_admin_user in under_admin_users:
				list_user_under_admin.append(under_admin_user['under_admin'])
			for user_iden_iter in user_iden_list:
				if  user_iden_list in list_user_under_admin:
					loc_data= models.user_location.objects.filter(user_iden=user_iden_iter).values('current_location')
					data_return[user_iden_iter]=loc_data[0]['current_location']
					location_sharing_obj=models.location_sharing.objects.create(event_id=event_id,user_iden=user_iden_req,user_loc_recv=user_iden_iter)
					print location_sharing_obj
				else:
					list_user_not_under_admin.append(user_iden_iter)
			if data_return:
				data={'loc_data':data_return,'not_authorized_for_user':list_user_not_under_admin}
				response_data=response_handling.send_response(data,iserror=False,error_code=200)
			else:
				response_data=response_handling.send_response(iserror=True,error_code=208)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def add_tag(request):
	if request.method=='POST':
		print request.POST
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		tag_name=request_rec['tag_name']
		if api_key is True:
			created_at=int(time.time())
			(tag_save,tag_status)=models.tag_table.objects.get_or_create(tag_name=tag_name,defaults={'created_at':created_at})
			print (tag_save,tag_status)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def list_tag(request):
	if request.method=='POST':
		print request.POST
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		if api_key is True:
			data_return=[]
			tag_datas=models.tag_table.objects.values('tag_name')
			for tag_data in tag_datas:
				data_return.append(tag_data['tag_name'])
			data={'tag_list':data_return}
			response_data=response_handling.send_response(data,iserror=False,error_code=200)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def event_completed(request):
	if request.method=='POST':
		print request.POST
		request_rec=ast.literal_eval(request.body)
		api_key=models.user_table.objects.filter(user_iden=request_rec['auth_token']).filter(isadmin=True).exists()
		if api_key is True:
			user_iden=request_rec['user_id']
			event_id=request_rec['event_id']
			event_id_obj=models.event_table.objects.get(event_id=event_id)
			user_id_obj=models.user_table.objects.get(user_iden=user_iden)
			event_completed_status=models.event_member.objects.filter(Q(event_id=event_id_obj)&Q(user_iden=user_id_obj)).update(event_completed=True)
			if event_completed_status==1:
				print 'Event completed.'
				event_completed_status=models.event_member.objects.filter(Q(event_id=event_id_obj)&~Q(user_iden=user_id_obj)).update(event_completed=None)
			elif event_completed_status>1:
				print 'More than one row affected.'
				#Enhancement: add verification to check for more than one row affected.
			else:
				print 'None of the rows got affected.'
				#Enhancement: add verification to check for None row affected.
			data={'event_id':event_id,'user_id':user_iden}
			response_data=response_handling.send_response(data,iserror=False,error_code=200)
		else:
			response_data=response_handling.send_response(not_found=True,error_code=203)
	else:
		response_data=response_handling.send_response(not_found=True,error_code=206)
	return HttpResponse(json.dumps(response_data), content_type="application/json")