from django.shortcuts import HttpResponse, render, redirect

def index(request):
    return render(request, 'index.html')