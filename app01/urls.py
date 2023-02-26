from django.urls import path

from . import views
from .views import music
urlpatterns = [
    path('', views.index.index, name='index'),
    path('music/list/', music.music_list)
]