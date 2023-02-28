from django.shortcuts import render, HttpResponse

# Create your views here.
def app02_index(request):
    return HttpResponse('app02 index')

def app02_index_1(reqeust, num):
    return HttpResponse(num)