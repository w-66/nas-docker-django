# Generated by Django 3.2 on 2023-03-09 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_loglife_lifelog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lifelog',
            old_name='title_text',
            new_name='title',
        ),
    ]
