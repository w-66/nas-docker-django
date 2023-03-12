from django.urls import path
from . import views

app_name = 'editormd'

urlpatterns = [
    path('', views.index, name='index'),
]