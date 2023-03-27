# -*- coding:utf-8 -*-
import django
from django.conf.urls import url
from django.urls import path
from .views import VditorImagesUploadView


urlpatterns = [
    path('uploads/', VditorImagesUploadView, name='uploads')
]
