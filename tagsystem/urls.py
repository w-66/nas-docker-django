from django.urls import path
from . import views

app_name = 'tagsystem'

urlpatterns = [
    path('', views.index, name='index'),

]