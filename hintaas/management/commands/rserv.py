'''
Created on Mar 31, 2014

@author: lauril
'''
import os
from django.core.management.base import BaseCommand


from django.conf import settings
from django.core import management
from autofixture.management.commands import loadtestdata
class Command(BaseCommand):
    args=''
    help='Start clean run.'

    def handle(self, *args, **options):
        self.stdout.write("Deleting sqlite.db\n" )
        try:
            self.stdout.write(settings.LOCAL_PATH + '/sqlite.db')
            os.remove(settings.LOCAL_PATH + '/sqlite.db')
        except Exception as e:
            self.stderr.write(str(e))
        
        self.stdout.write("Calling syncdb command\n" )
        management.call_command('syncdb', verbosity=1, interactive=False)
        self.stdout.write("Calling runserver command\n" )
        management.call_command('runserver', verbosity=1, interactive=False)    
        

