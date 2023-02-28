from django.db import models

# Create your models here.
class App02Lifelog(models.Model):
    global_id = models.PositiveBigIntegerField(verbose_name="ID", primary_key=True)
    addtime = models.DateTimeField(verbose_name="添加时间")
    tag = models.CharField(verbose_name="分类", default="日常", max_length=128, blank=False, null=False)
    content = models.TextField(verbose_name="内容")

    location_id_choices = (
            (0, '无'), (1, '环卫局宿舍'), (2, '奥莱'), (3, '老家')
        )
    location_id = models.IntegerField(verbose_name="地址", db_column='location_Id', choices=location_id_choices, default=2)  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'app01_lifelog'
