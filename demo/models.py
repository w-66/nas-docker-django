from django.db import models
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    name_ch = models.CharField(verbose_name="电影名称(中)", max_length=100, unique=True)
    name_en = models.CharField(verbose_name="电影名称(英)", max_length=100)
    movie_synopsis = models.TextField(verbose_name="电影简介", null=True)

class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=10)
    content = models.TextField(verbose_name='内容')
    pub_date = models.DateTimeField(verbose_name='发布时间',default=timezone.now)
    
    def __str__(self):
        return self.title