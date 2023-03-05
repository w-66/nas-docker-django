from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name='index'),

    path('navbar/1/', views.navbar1, name='navbar1'),
    path('navbar/2/', views.navbar2, name='navbar2'),
    path('test/1/', views.test1, name='test1'),

]