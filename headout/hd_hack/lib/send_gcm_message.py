from hd_hack import models

def send_message_gcm(gcm_ids,message):
	status_return={}
	for gcm_id in gcm_ids:
		gcm_id=models.gcm_table.objects.get(gcm_id=gcm_id)
		created_at=int(time.time())
		obj_gcm_text=models.gcm_text.objects.create(gcm_id=gcm_id,message=message,created_at=created_at)
		###IMPLEMENT SENDING DATA
		status_gcm_send=True
		#gcm_id=models.ForeignKey(gcm_table)	
		#message=models.TextField()
		#created_at=models.CharField(max_length=30)
		if status_gcm_send is True:
			status_return[gcm_id]=True
		else:
			status_return[gcm_id]=False
	return status_return