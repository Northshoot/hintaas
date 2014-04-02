from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

    
class Profile(models.Model):
    user=models.ForeignKey(User, unique=True)
    company = models.CharField(max_length=40)
    created =  models.DateTimeField(auto_now_add=True)
    updated_local =  models.DateTimeField(blank=True, null=True)

    
    
    def save(self,*args,**kwargs):
        self.updated_local = datetime.now()
        super(Profile, self).save(*args,**kwargs)
    
    def __unicode__(self):
        return "Profile: %s" %self.user
    
class AwsCredential(models.Model):
    user=models.ForeignKey(User, unique=False)
    status=models.BooleanField(blank=False, null=False)
    created=models.DateField(null=False)
    access_key_id=models.CharField(max_length=30)
    secret_access_key=models.CharField(max_length=40)
    aws_user_id = models.CharField(max_length=50)
    arn = models.CharField(max_length=100)
        
    def __unicode__(self):
        return "AwsCredentials for %s" %self.user
    
    def getSecret(self):
        return "%s" %self.secret_access_key
    

    
