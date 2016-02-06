#!/bin/bash
bash install_req.sh
if [ $? -ne 0 ]; then
echo 'Installing req dependencies failed.'
else
echo 'Installing req dependencies passed.'
cd headout_hack/headout
nohup /usr/bin/python manage.py runserver 0.0.0.0:8080 >/dev/null 2>&1 &
if [ `ps aux | grep -v grep| grep -c manage.py` -gt 0 ]; then
echo 'The Server is running succesfully.You can logout now.'
fi
fi