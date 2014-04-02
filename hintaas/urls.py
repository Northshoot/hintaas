from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from testrunner import urls as runner_urls
admin.autodiscover()
import autofixture
autofixture.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hintaas.views.home', name='home'),
    
    url(r'^template/(?P<action>\w+)/$', 'hintaas.views.template', name='template'),
    url(r'^template/run/(\d+)/$', 'testrunner.views.runTest', name='runTest'),
    url(r'^inter/(?P<action>\w+)/','hintaas.views.inter',name='interoperability'),
    url(r'^runner/',include(runner_urls)),
    # url(r'^HinTaaSource/', include('HinTaaSource.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
