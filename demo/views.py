from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
    return render(request, 'demo/index.html')

def navbar1(request):
    return render(request, 'demo/navbar1.html',)

def navbar2(request):
    return render(request, 'demo/navbar2.html',)

def test1(request):

    return render(request, 'demo/test1.html')
    
def test2(request):

    return render(request, 'demo/test2.html')
    
def test3(request):
    return render(request, 'demo/test3.html')
    
def test4(request):
    return render(request, 'demo/test4.html')
    