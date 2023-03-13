from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Lifelog, Article

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

# import markdown
from django import forms

class Article_ListView(generic.ListView):
    # pass
    template_name = 'blog/article_list.html'
    context_object_name = 'queryset'
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 记得在顶部引入 markdown 模块
    # article.content = markdown.markdown(article.content,
    #                               extensions=[
    #                                  'markdown.extensions.extra',
    #                                  'markdown.extensions.codehilite',
    #                                  'markdown.extensions.toc',
    #                               ])
    return render(request, 'blog/article_detail.html', context={'article': article})

# 在 Form 中使用 markdown 编辑字段
class ArticleMDEditorModleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

# 在前端使用markdown编辑器
def article_change(request, pk):
    """新增; 修改 使用markdown编辑器; """
    if request.method == "GET":
        form = ArticleMDEditorModleForm()
        return render(request, 'blog/article_change.html', {'form':form})

    form = ArticleMDEditorModleForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')