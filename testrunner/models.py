from django.db import models
from django.contrib.auth.models import User
from testset.models import TestTemplate
# Create your models here.

class TestBacker(models.Model):
    user = models.ForeignKey(User)
    template= models.ForeignKey(TestTemplate)
    request_time = models.DateTimeField(auto_now=True)
    test_status = models.CharField(max_length=30)
    instance_status = models.CharField(max_length=30)
    ami_name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return "%s running test %s: started: %s, Test status: %s Instance status: %s"%(
                                                               self.user.name,
                                                               self.template.name,
                                                               self.request_time,
                                                               self.test_status,
                                                               self.instance_status)
        
    def getStatus(self):
        return self.status
    
    def updateStatus(self, status):
        self.status = status
        self.save(commit=True)