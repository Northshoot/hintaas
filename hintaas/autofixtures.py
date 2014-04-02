'''
Created on Apr 1, 2014

@author: lauril
'''
    
from autofixture import generators, register
from autofixture.base import AutoFixture    
from tests.models import TestTemplate
from datetime import datetime
import random
import string

class ImageNameGenerator(generators.Generator):
    
    def generate(self):
        return 'i-'+str(self.id_generator(size=10))

    def id_generator(self,size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

import autofixture
list = autofixture.create('tests.models.TestTemplate', 10, 
                     field_values={
                                  'image': ImageNameGenerator(),
                                  'image': generators.FirstNameGenerator(),
                                  'image': generators.StaticGenerator('test_template.xml'),
                                  'image': generators.LoremGenerator(max_length=300),
                                  'image': staticmethod(lambda: random.choice((10,200))),
                                  'image': generators.StaticGenerator('https://localhost:9493')
                                  
                                  })

print list