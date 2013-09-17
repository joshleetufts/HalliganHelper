__author__ = 'tyler'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('HalliganComputerAvailability.views',
    url(r'^$', 'ApiDocs', name='docs'),
    url(r'^all/$', 'AllComps', name='AllComps'),
    url(r'^room/(?P<RmNum>.+)/$', 'SpecificRoom', name='SpecificRoom'),
    url(r'^machine$', 'SpecificMachine', name='SpecificMachine'),
    url(r'^update/(?P<MchID>.+)/(?P<NewStatus>.+)', 'UpdateStatus', name='UpdateStatus'),
    url(r'^updateServer/(?P<MchID>.+)/(?P<NewStatus>.+)/(?P<NumUsers>\d+)', 'UpdateServer', name='UpdateServer'),
)