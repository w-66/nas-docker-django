"""django_www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # 网易爬虫
    path('crawler/music/', views.crawler_music),
    # 音乐列表编辑页
    path('music/list/edit/<int:global_id>/', views.music_list_edit),
    # 音乐列表
    path('music/list/', views.music_list),
    # 测试
    path('demo/text/', views.demo_text),
    # path('admin/', admin.site.urls),
]
