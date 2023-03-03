from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
    return render(request, 'demo/index.html')

def navbar1(request):
    return render(request, 'demo/navbar1.html', {"title":'navbar1'})
def navbar2(request):
    return render(request, 'demo/navbar2.html', {"title":'navbar2'})