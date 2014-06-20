from __future__ import absolute_import

from djproj.celery import app
from celery import task
from celery import shared_task
import datetime
from datetime import timedelta

@shared_task
def autodiscovertask1():
    currt = datetime.datetime.now()
    with open("files/autodiscovertask1.txt", "w") as fo:
        print >> fo, currt.isoformat()+"autodiscovertask_1"
    return currt.isoformat()

@shared_task
def autodiscovertask2():
    print "========[autodiscovertask2]========"

