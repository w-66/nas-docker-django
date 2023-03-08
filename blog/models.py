from django.db import models

# Create your models here.
class Lifelog(models.Model):
    title_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title_text

class Tag(models.Model):
    title = models.ForeignKey(Lifelog, on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=200)
    def __str__(self):
        return self.tag_text