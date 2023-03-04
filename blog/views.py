from django.shortcuts import render


def index(request):
    title = 'Blog'
    return render(request, 'blog/index.html', {'title':title})
def log(request):
    return render(request, 'blog/lifelog.html')