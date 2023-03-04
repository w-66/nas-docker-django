import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 使用 display() 装饰器来改进
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
        )
    def was_published_recently(self):
        '''如果 Question 是在一天之内发布的， 
           Question.was_published_recently() 方法将会返回 True'''
        ### v3 优化代码，增加可读性
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
        ## self.pub_date 实例对象的发布时间
        ## timezone.now()现在时间 
        ## datetime.timedelta(days=1) 一天的时间
        ### v2 修复bug，未来时间，显示true
        # return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        ### v1 
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    # 自动生成的代码，之后用到了再看
    # class Meta:
    #     verbose_name = _("Question")
    #     verbose_name_plural = _("Questions")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Question_detail", kwargs={"pk": self.pk})
