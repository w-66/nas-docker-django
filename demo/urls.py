from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name='index'),

    path('navbar/', views.navbar, name='navbar')

]