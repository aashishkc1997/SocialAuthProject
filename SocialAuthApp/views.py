
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def function_socialhome(request):
    print('socialhome',request.user)
    return render(request, 'index.html')

@login_required
def function_signedin(request):
    context = {
        'user': request.user
        if request.user.is_authenticated else []
    }
    print('signed in ', request.user)
    request.user
    request.user.is_active = True
    request.user.save()

    return render(request, 'signedin.html',context)


def glogout(request):
    print('glogout', request.user)
    if request.user.is_authenticated:
        request.user.is_active = False
        request.user.save()
        request.user=None
    return function_socialhome(request)