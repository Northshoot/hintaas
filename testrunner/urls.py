'''
Created on Apr 2, 2014

@author: lauril
'''
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^(\d+)/$', 'testrunner.views.runTest', name='runTest'),
                       url(r'^status/$', 'testrunner.views.runStatus', name='runStatus'),
                       )