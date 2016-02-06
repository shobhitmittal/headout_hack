import time
import string
import random

def send_response(data=None,iserror=False,not_found=False,error_code=200):
	if not_found is True:
		response_data={'data':'no post request received','code':error_code}
	if iserror is False and not_found is False:
		response_data= {'data': data,'code':error_code}
	elif iserror is True and not_found is False:
		response_data= {'code':error_code}
	else:
		print 'invalid argument passed in send_response function.Value is :'+str(iserror)
	return response_data

def generate_random(length=25):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))