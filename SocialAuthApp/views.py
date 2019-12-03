
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
# Create your views here.
from django.template import RequestContext


def function_socialhome(request):
    request.user = None
    print('socialhome',request.user)
    return render(request, 'index.html')

@login_required
def function_signedin(request):
    print('signedin',request.user)
    request.user.is_active=False
    request.user.save()
    context = {
        'x':'x'
        if request.user.is_authenticated else []
    }
    return render(request, 'signedin.html',context)


def glogout(request):
    print('glogout', request.user)
    request.user.is_active=False
    request.user.save()
    auth_logout(request)
    return redirect('/')