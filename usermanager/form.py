'''
Created on Jul 20, 2012

@author: lauril
'''
from django import forms
from django.contrib.auth.models import User
from usermanager.models import Course, Profile
from registration.forms import RegistrationForm
from django.utils.translation import ugettext_lazy as _



attrs_dict = { 'class': 'required' }


        
def affiliation_valid_email(value):
    allowed_domain=['student.ltu.se','ltu.se']
    if value.split('@')[1] not in allowed_domain:
        raise forms.ValidationError(_("Email does not match allowed domains (student.ltu.se, ltu.se)"))
    else:
        return value


   
class UserRegistrationForm(RegistrationForm):  
    
    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email", "password1", "password2")
        
    username = forms.RegexField(regex=r'^\w',
                                max_length=9,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username - same as in LTU!"),
                                error_messages={ 'invalid': _("User name needs to match LTU convention.") })
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    course = forms.ModelChoiceField(queryset=Course.objects,required=True)
    email = forms.EmailField(validators=[affiliation_valid_email],
                             widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),label=_("LTU - Email address"))
    

    
    def clean(self):
        super(UserRegistrationForm, self).clean()
        print self.cleaned_data
        if self.cleaned_data['email'].split('@')[0] == self.cleaned_data.get("username"):
            return self.cleaned_data
        else:
            raise forms.ValidationError(_("Email and user name do not match."))
         
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)    
        user.email = self.cleaned_data["email"]
        user.first_name =  self.cleaned_data["first_name"]
        user.last_name =self.cleaned_data["last_name"]
        profile = Profile(systemuser=user,
                                            course=self.cleaned_data["course"])

        
        user.save()
        profile.save()
        return user
