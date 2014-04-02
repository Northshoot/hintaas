'''
Created on Apr 1, 2014

@author: lauril
'''
from django.db import models
from usermanager.models import Profile

class Service(models.Model):
    user = models.ForeignKey(Profile)
    name = models.CharField(max_length=30)
    description  = models.CharField(max_length=300)

    class Meta:
        abstract = True
        
class ServiceProvider(Service):
    def __unicode__(self):
        return 'Service %s provided by %s' %(self.name,self.user.company)

class ServiceConsumer(Service):
    def __unicode__(self):
        return 'Service %s consumed by %s' %(self.name,self.user.company)    
    
class Interoperability(models.Model):
    provider = models.ForeignKey(ServiceProvider)
    consumer =models.ForeignKey(ServiceConsumer)
    compatible = models.BooleanField(default=False)
    
    def __unicode__(self):
        ret ='%s is ' %self.provider
        print dir(self.provider)
        if not self.compatible:
            ret+='not '
        ret+='compatible with %s' %self.consumer
        return ret