from __future__ import absolute_import

import os
import datetime
from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djproj.settings')

app = Celery('djproj')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#import apps.app1.tuan

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task
def defaulttask1():
    currt = datetime.datetime.now()
    with open("files/defaulttask1.txt", "w") as fo:
        print >> fo, currt.isoformat()+"default_task_1"
        return currt 

@app.task
def hello():
    print "helloincelery" 
