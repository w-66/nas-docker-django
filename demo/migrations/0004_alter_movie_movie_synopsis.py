# Generated by Django 3.2 on 2023-03-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_alter_movie_name_ch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_synopsis',
            field=models.TextField(null=True, verbose_name='电影简介'),
        ),
    ]