# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('content.html',dict(user=request.user),RequestContext(request))


