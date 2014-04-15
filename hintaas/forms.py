# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from models import ServiceConsumer, ServiceProvider, Service
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field,Fieldset, ButtonHolder
PROVIDER = (
            (0, 'Provider'),
            (1, 'Consumer'),
            )

class ServiceCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.form_class ='form-horizontal'
        self.helper.help_text_inline = True
        self.helper.error_text_inline = False
        self.helper.layout = Layout(
                Fieldset(
                         '',
                         'name',
                         'description',
                         'provider',                   
                         ),
                ButtonHolder(
                    HTML('<div class="floating-menu">'),
                    Submit('submit', 'Save', css_id='submit', css_class='btn btn-success'),
                    HTML("<input type='button' name='cancel' value='Close' onclick='self.close ()' class='btn btn-danger'> </div>")
                )
            )
        
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    provider = forms.IntegerField(widget=forms.Select(choices=PROVIDER))
    
    class Meta:
        model = Service
    
class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        
class ServiceConsumerForm(forms.ModelForm):
    class Meta:
        model = ServiceConsumer