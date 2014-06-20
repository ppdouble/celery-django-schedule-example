from __future__ import absolute_import

from djproj.celery import app
from celery import task
from celery import shared_task
import datetime

#@shared_task
#def add(x, y):
#    return x + y

#@shared_task
#def mul(x, y):
#    return x * y

#@shared_task
#def xsum(numbers):
#    return sum(numbers)

@app.task
def tuantask1():
    currt = datetime.datetime.now()
    with open("files/tuantask1.txt", "w") as fo:
        print >> fo, currt.isoformat()+"tuantask_1"
    return currt.isoformat()

@app.task
def tuantask2():
    print "stest===="
