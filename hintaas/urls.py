from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from testrunner import urls as runner_urls

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hintaas.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include('auth_users.urls')),
    url(r'^template/(?P<action>\w+)/$', 'hintaas.views.template', name='template'),
    url(r'^template/', include('testrunner.urls')),
    url(r'^service/list/(?P<action>\w+)/$', 'hintaas.views.services', name="services"),
    url(r'^service/add/$', 'hintaas.views.serviceAdd', name="serviceAdd"),
    url(r'^inter/(?P<action>\w+)/','hintaas.views.inter',name='interoperability'),
    url(r'^runner/',include(runner_urls)),
    url(r'analytics/', 'hintaas.views.analytics', name='analytics'),
    # url(r'^HinTaaSource/', include('HinTaaSource.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    
)
