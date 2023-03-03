from django.urls import path
from . import views

app_name = 'me'

urlpatterns = [
    path('', views.index, name='index'),
]