# Generated by Django 3.2 on 2023-03-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20230311_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifelog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='标签'),
        ),
    ]
