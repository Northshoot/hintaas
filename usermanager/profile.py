from django import forms
from models import Profile

from registration.forms import RegistrationForm

class ProfileForm(forms.Form):
    
    def save(self, user):
        try:	
            data = user.get_profile()
        except:
            data = Profile(user=user)
        

        data.save()
        
class UserRegistrationForm(RegistrationForm):
    course = forms.ModelChoiceField()