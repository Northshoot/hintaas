from django.db import models

# Create your models here.
class TestTemplate(models.Model):
    image = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    configuration_xml = models.CharField(max_length=50)#upload_to='test_configs/%Y/%m/')
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now=True)#auto_add=True
    back_end_url= models.CharField(max_length=70)
    
    
    def __unicode__(self):
        return "Test %s created on %s, image: %s." %(self.name, self.created_date,self.image)
