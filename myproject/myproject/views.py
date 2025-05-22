from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def homepage(request):
    #return HttpResponse("Hello World! I'm Home.")
    return render(request, 'index.html')

def force_logout(request):
    logout(request)
    return redirect('/')