from __future__ import absolute_import

from celery import shared_task
import datetime

@shared_task
def mytask1():
    currt = datetime.datetime.now()
    with open("files/mytask1.txt", "w") as fo:
        print >> fo, currt.isoformat()+"mytask_1"
    return currt.isoformat()

@shared_task
def mytask2():
    print "========[mytask2]========"
