from django.shortcuts import render, redirect, HttpResponse

def chart_list(request):

    return render(request, "chart.html")