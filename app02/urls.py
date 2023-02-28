from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.app02_index, name='app02_index'),
    path('index/<int:num>/', views.app02_index_1, name=''),
]