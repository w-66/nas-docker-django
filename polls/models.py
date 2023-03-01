import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
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
