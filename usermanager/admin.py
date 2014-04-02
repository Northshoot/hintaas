'''
Created on Jul 19, 2012

@author: lauril
'''
from django.contrib import admin
from models import Profile,AwsCredential


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','company','created')
    list_filter = ('created',)
    search_fields =('company','user')
    

admin.site.register(Profile, ProfileAdmin)
admin.site.register(AwsCredential)


