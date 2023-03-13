from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('lifelog/', views.Lifelog_ListView.as_view(), name='lifelog'),
    # path('lifelog/<int:pk>', views.Lifelog_DetailView.as_view(), name='lifelog_detail'),
    path('article/', views.Article_ListView.as_view(), name='article_list'),
    path('article/<int:pk>', views.article_detail, name='article_detail'),
    path('article/<int:pk>/change/', views.article_change, name='article_change')

]