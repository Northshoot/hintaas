from django.conf.urls import patterns, include, url
from usermanager.views import home
from cloud import urls as cloud_urls
from form import UserRegistrationForm

from regbackend import StudentBackend
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/register/$',
        StudentBackend.as_view(form_class = UserRegistrationForm),
        name='registration_register'),
    
    (r'^accounts/', include('registration.backends.default.urls')),
     url(r'^admin/', include(admin.site.urls)),
    url(r'user/', home),
    url(r'cloud/',include(cloud_urls)),
    url(r'^$', home),  
)
