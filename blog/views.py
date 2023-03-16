from django.shortcuts import render
from django.views import generic
from .models import Lifelog

# 网页图标logo
# site_logo = 'icon-logo-1' 替换成本地路径的logo
def index(request):
    title = 'Blog'
    dict = {
        'title':title,
    }
    return render(request, 'blog/index.html', dict)
    

class Lifelog_ListView(generic.ListView):
    template_name = 'blog/lifelog.html'
    context_object_name = 'queryset'
    paginate_by = 6
    def get_queryset(self):
        return Lifelog.objects.order_by('-pub_date')

# def lifelog(request):    
#     return render(request, 'blog/lifelog.html')

# class Lifelog_DetailView(generic.DetailView):
#     model = Lifelog
#     template_name = 'blog/detail.html'

#     def get_queryset(self):
#         return Lifelog.objects

from django import forms

class Article_ListView(generic.ListView):
    # pass
    template_name = 'blog/article_list.html'
    context_object_name = 'queryset'
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')

