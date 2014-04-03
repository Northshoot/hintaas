# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from datetime import datetime
import json
from models import TestBacker
from cloudmanager import instanceRunner as ir
from django.contrib.auth.models import User
from models import TestTemplate


def runTest(request, tid):
#     tb = TestBacker()
#     tb.user = User.objects.get(pk=request.user)
#     #tb.template= TestTemplate.objects.get(pk=1)
#     tb.ami_name='ami-43fa0234'
#     tb.instance_status = 'Initializing'
#     tb.ami_name = 'Initializing'
#     tb.save()
    return render_to_response('test_runner.html',dict(test="RUN template %s" %str(tid),
                                                                            runner=5),RequestContext(request))


def runStatus(request):
    print request.is_ajax()
    counter = int( request.REQUEST['counter'])
    data={'status':'STARTING', 'time':str(datetime.now()), 'counter':counter+1}
    return HttpResponse(json.dumps(data))
