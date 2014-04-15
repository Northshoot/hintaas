'''
Created on Jul 20, 2012

@author: lauril
'''


from registration.backends.default.views import RegistrationView


#create custom registration backend
class StudentBackend(RegistrationView): 
    '''
    we just want to override register and fix profile creation etc
    ''' 
    def register(self,request, **kwargs):
        from usermanager.models import Profile
        user=super(StudentBackend,self).register(request, **kwargs)
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.save()
        profile = Profile.objects.create(user=user, company=kwargs['company'])
        profile.save()
        
    def get_form_class(self, request):
        """
        Return the default form class used for user registration.

        """
        from usermanager.form import UserRegistrationForm
        return UserRegistrationForm    
