from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('lifelog/', views.Lifelog_ListView.as_view(), name='lifelog'),
    # path('lifelog/<int:pk>', views.Lifelog_DetailView.as_view(), name='lifelog_detail'),

]