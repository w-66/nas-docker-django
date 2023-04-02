# Generated by Django 3.2 on 2023-03-22 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_alter_movie_movie_synopsis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
            ],
        ),
    ]