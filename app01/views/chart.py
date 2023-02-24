from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def chart_list(request):
    return render(request, "chart.html")

def chart_bar_ajax(request):
    title = [{
        "text": 'ECharts 入门示例3'
    }]
    xAxis = [{  
        "type": 'category',
        "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        "axisTick": {
            "alignWithLabel": True
        }   
    }]
    series = [{
        "name": 'Direct',
        "type": 'bar',
        "barWidth": '60%',
        "data": [10, 52, 200, 33, 444, 330, 220]
    }]
    result = {
        "status": True,
        "data": {
            'title' : title,
            'xAxis' : xAxis,
            'series': series
        }
    }
    return JsonResponse(result)

    
