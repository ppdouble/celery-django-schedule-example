from __future__ import absolute_import

from djproj.celery import app
from celery import task
from celery import shared_task
import datetime
from datetime import timedelta
#@shared_task
#def add(x, y):
#    return x + y

#@shared_task
#def mul(x, y):
#    return x * y

#@shared_task
#def xsum(numbers):
#    return sum(numbers)

#app.config.update(
#CELERYBEAT_SCHEDULE = {
    #'defaulttask1': {
    #    'task': 'djproj.celery.defaulttask1',
    #    'schedule': timedelta(seconds=3)
    #}, 
    #'hello': {
    #    'task': 'djproj.celery.hello',
    #    'schedule': timedelta(seconds=4)
    #}, 
    #'tuantask1': {
   #     'task': 'apps.app1.tasks.tuantask1',
  #      'schedule': timedelta(seconds=6)
 #   },  
    #'tuantask2': {
    #    'task': 'app1.tuan.tuantask2',
    #    'schedule': crontab(minute=55, hour=17)
    #}

#
#}

@app.task
def tuantask1():
    currt = datetime.datetime.now()
    with open("files/tuantask1.txt", "w") as fo:
        print >> fo, currt.isoformat()+"tuantask_1"
    return currt.isoformat()

@app.task
def tuantask2():
    print "stest===="

app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'tuantask1': {
            'task': 'apps.app1.tasks.tuantask1',
            'schedule': timedelta(seconds=6)
        },  
    }
)
