from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('HELLO WORLD')
    return render(request,'about.html')

def home(request):
    # return HttpResponse('This is my HOMEPAGE')
    return render(request, 'home.html')
