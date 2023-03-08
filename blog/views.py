from django.shortcuts import render

# 网页图标logo
# site_logo = 'icon-logo-1' 替换成本地路径的logo
def index(request):
    title = 'Blog'
    dict = {
        'title':title,
    }
    return render(request, 'blog/index.html', dict)
    
def lifelog(request):
    
    return render(request, 'blog/lifelog.html')

