# Generated by Django 3.2 on 2023-03-09 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230309_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='votes',
        ),
        migrations.AlterField(
            model_name='lifelog',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
