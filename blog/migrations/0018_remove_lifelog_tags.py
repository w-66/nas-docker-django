# Generated by Django 3.2 on 2023-03-11 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_lifelog_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lifelog',
            name='tags',
        ),
    ]
