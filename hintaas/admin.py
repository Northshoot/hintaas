'''
Created on Apr 1, 2014

@author: lauril
'''
from django.contrib import admin
from models import ServiceProvider, ServiceConsumer,Interoperability

admin.site.register(ServiceProvider)
admin.site.register(ServiceConsumer)
admin.site.register(Interoperability)