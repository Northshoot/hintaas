from django.conf.urls import patterns, include, url

from form import UserRegistrationForm

from regbackend import StudentBackend


urlpatterns = patterns('',
    url(r'^accounts/register/$',
        StudentBackend.as_view(form_class = UserRegistrationForm),
        name='registration_register'),


)
