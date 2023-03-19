from django.db import models

# Create your models here.
class Movie(models.Model):
    name_ch = models.CharField(verbose_name="电影名称(中)", max_length=100, unique=True)
    name_en = models.CharField(verbose_name="电影名称(英)", max_length=100)
    movie_synopsis = models.TextField(verbose_name="电影简介", null=True)