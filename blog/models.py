from django.db import models
from django.utils import timezone

# 为了动态计算每个标签的引用次数
from django.db.models.signals import m2m_changed, pre_delete
from django.dispatch import receiver

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(verbose_name='标签名', unique=True, max_length=200)
    references_count = models.IntegerField(verbose_name='引用次数', default=0)
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

    def __str__(self):
        return self.content


### v2 解决v1的问题
@receiver(m2m_changed, sender=Lifelog.tags.through)
def update_tag_references_count(sender, instance, action, model, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear', 'reverse']:
        for tag in instance.tags.all():
            tag.references_count = tag.lifelog_set.count()
            tag.save()
        if action == 'post_remove' or action == 'post_clear':
            for tag_pk in kwargs['pk_set']:
                tag = model.objects.get(pk=tag_pk)
                tag.references_count = tag.lifelog_set.count()
                tag.save()
@receiver(pre_delete, sender=Lifelog)
def delete_lifelog(sender, instance, **kwargs):
    for tag in instance.tags.all():
        tag.references_count = tag.lifelog_set.exclude(pk=instance.pk).count()
        tag.save()

### v1 在添加行记录时能执行if中的内容，而修改tag，或者删除lifelog记录时，都不会更新tag.references_coun的问题
# @receiver(m2m_changed, sender=Lifelog.tags.through)
# def update_tag_references_count(sender, instance, action, model, **kwargs):
#     if action == 'post_add' or action == 'post_remove' or action == 'reverse':
#         for tag in instance.tags.all():
#             tag.references_count = tag.lifelog_set.count()
#             tag.save()


#####
# from mdeditor.fields import MDTextField

class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=10)
    content = models.TextField(verbose_name='内容')
    pub_date = models.DateTimeField(verbose_name='发布时间',default=timezone.now)
    
    def __str__(self):
        return self.title