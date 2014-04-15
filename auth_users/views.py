# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

def log_in_user(request):
    state = "Please login"
    usr = psw = ''
    if request.POST:        
        usr = request.POST.get('username')
        psw = request.POST.get('password')
        user = authenticate(username=usr, password=psw)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You have been logged in."
                print request.POST.get('remember-me')
                if request.POST.get('remember-me'):
                    pass
                else:
                    request.session.set_expiry(1000)
                next_=request.POST.get('next', None)
                if not next_:
                    next_ ='/'
                return redirect(next_)
            else:
                state = "Your account is inactive, contact administrator"
        else:
            state = "Username or password is incorect"
            return render_to_response('auth/login.html',{'state':state, 'username': usr, 'next':next},context_instance=RequestContext(request))
    else:
        return render_to_response('auth/login.html',
                                  {'state':state, 
                                   'username': usr,
                                   'next':request.GET.get('next',None)
                                   },RequestContext(request))



def log_out_user(request):
    logout(request)
    return redirect('/')

