# Generated by Django 3.2 on 2023-03-09 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_lifelog_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag_text',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='title',
        ),
        migrations.AddField(
            model_name='lifelog',
            name='tag',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lifelog',
            name='title_text',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
