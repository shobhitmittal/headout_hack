import requests
from hd_hack import models
from django.db.models import Q

def event_completed(user_id,url,payload):
	confirm_callback=models.user_table.objects.filter(Q(isadmin=True) & Q(user_iden=user_id)).exists()
	if confirm_callback is True:
		req=requests.post(url,payload=json.dumps(payload))
		if req.status_code==requests.codes.ok:
			print 'Webhook call successful'
		else:
			print 'Webhook call unsuccessful'
	else:
		print 'User_id provided don`t have admin permissions.'

                                                                                                                                                                                                 

