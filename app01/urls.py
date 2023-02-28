from django.urls import path

from . import views
from .views import music, learn_bootstrap
urlpatterns = [
    path('', views.index.index, name='index'),
    path('music/list/', music.music_list),
]