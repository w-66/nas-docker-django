from django.db import models

# Create your models here.
class Loglife(models.Model):
    title_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', default='2023-03-05')
    tag_text = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.ForeignKey(Loglife, on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text