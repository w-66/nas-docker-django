# Generated by Django 3.2 on 2023-03-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230305_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='loglife',
            name='pub_date',
            field=models.DateTimeField(default='2023-03-05 02:22:29.657077000', verbose_name='date published'),
        ),
    ]