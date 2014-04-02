# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from datetime import datetime
import json


def runTest(request, tid):
    return render_to_response('test_runner.html',dict(test="RUN template %s" %str(tid)),RequestContext(request))


def runStatus(request):
    print request.is_ajax()
    counter = int( request.REQUEST['counter'])
    data={'status':'STARTING', 'time':str(datetime.now()), 'counter':counter+1}
    return HttpResponse(json.dumps(data))
