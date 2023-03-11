from django.db import models
from django.utils import timezone



# Create your models here.

class Tag(models.Model):
    tag = models.CharField(verbose_name='标签名', unique=True, max_length=200)
    def __str__(self):
        return self.tag

class Lifelog(models.Model):
    # now = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    pub_date = models.DateTimeField(verbose_name='发布时间',default=timezone.now)
    content = models.TextField(verbose_name='内容', null=True)
    location_choices = (
        (0, '无'), (1, '环卫局宿舍'), (2, '奥莱'), (3, '老家')
    )
    location = models.PositiveSmallIntegerField(verbose_name='位置',choices=location_choices, default=2)

    # tag_choices = [(tag.id, tag.tag) for tag in Tag.objects.all()]  
    # tag = models.SmallIntegerField(null=True, blank=True,verbose_name='标签',help_text='一个tag')
    # tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='标签')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

        
    # def __str__(self):
    #     return self.content

