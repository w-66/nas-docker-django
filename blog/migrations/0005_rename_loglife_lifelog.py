# Generated by Django 3.2 on 2023-03-08 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_loglife_pub_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loglife',
            new_name='Lifelog',
        ),
    ]
