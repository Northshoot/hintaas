'''Created on 30 apr 2013
Python class that manages worker instances
@author: didier gourillon
'''

from boto.ec2.connection import EC2Connection 
import time
import socket 
import os,datetime, sys
import threading
GROUPNAME = 'MAESTRO'
CLIENT_PORT = 9999

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/Users/lauril/workspace/hintaas/ccmd.srv.log',
                    filemode='w+')
boto_log = logging.getLogger('boto')
boto_log.setLevel(logging.WARNING)
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
logger = logging.getLogger('hintaas.cloud.instancerunner')

def log(msg):
    logger.debug(msg)



# This class handles instance Management
class InstanceRunner(threading.Thread):    
    def __init__(self,threadID, name='Instance Runner Thread', ami_name='ami-43fa0234',
                        delay=5000, region='eu-west-1'):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.delay = delay
        self.name = name
        self.region=region
        self.conn = EC2Connection()
        self.ami_name =ami_name
        self.reservation = None
        self.instance_ip =[]
        
    def run(self):
        try:
            self.reservation=self.conn.run_instances(
                                         self.ami_name,
                                         instance_type='t1.micro',
                                         security_groups=['hintaas'])
            self.instance_ip = self.update_Running_Instances()
            print self.instance_ip
        except Exception as e:
            logger.critical("Can't start instance %s" %e)
            raise

    def update_Running_Instances(self): 
        boolean_pending = True 
        # this boolean will be set to True everytime an instance qith a 'pending state' is found 
        while boolean_pending:
                    for current_instance in self.reservation.instances:
                        print current_instance.state
                        # if an instance has a pending state we still have to wait for it to have an ip address
                        if (current_instance.state == 'pending'):
                            log( " waiting for "+current_instance.instance_type+" booting instance " +current_instance.id)
                            boolean_pending = True
                            
                            time.sleep(60)
                        # if an instance has a running state we can register its ip address
                        elif (current_instance.state == 'running') :
                            #print "dns ", current_instance.public_dns_name 
                            current_instance.add_tag('Name', 'Runner of ' + self.ami_name)
                            current_instance.add_tag('Started', datetime.datetime.now())
                            current_instance.add_tag('user', 'lauril')
                            self.instances_types[current_instance.public_dns_name ] = current_instance.instance_type
                            self.ip_addresses[str(current_instance.id)] = current_instance.public_dns_name  
                            time.sleep(60)
                            boolean_pending = False
                            
        new_ips = []
        for value in self.ip_addresses.values():
            new_ips.append(str(value))
        return new_ips     
    
if __name__ == "__main__":
    ir = InstanceRunner(1)
    ir.start()