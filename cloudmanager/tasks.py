'''
Created on Mar 31, 2014

@author: lauril
'''
from __future__ import absolute_import

from celery import shared_task




@shared_task
def cleanEBS(x,y):
    return x*y