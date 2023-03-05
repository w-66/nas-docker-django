from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
    return render(request, 'demo/index.html')

def navbar1(request):
    function_name = navbar1.__name__
    return render(request, 'demo/navbar1.html', {"title":function_name})

def navbar2(request):
    function_name = navbar2.__name__
    return render(request, 'demo/navbar2.html', {"title":function_name})

def test1(request):
    function_name = test1.__name__
    return render(request, 'demo/test1.html',{"title":function_name})
    