from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def index(request):
    return render(request, 'demo/index.html')

def navbar(request):
    return render(request, 'demo/navbar1.html', {"title":'navbar'})