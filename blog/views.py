from django.shortcuts import render

# 网页图标logo
# site_logo = 'icon-logo-1' 替换成本地路径的logo
def index(request):
    title = 'Blog'
    dict = {
        'title':title,
        'site_logo':site_logo,
    }
    return render(request, 'blog/index.html', dict)
def log(request):

    return render(request, 'blog/lifelog.html', {'site_logo':site_logo})

