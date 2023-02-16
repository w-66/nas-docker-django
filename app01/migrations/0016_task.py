# Generated by Django 3.2 on 2023-02-16 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_alter_admin_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urgency', models.SmallIntegerField(choices=[(3, '紧急'), (2, '一般'), (1, '松弛')], default=1, verbose_name='紧急程度')),
                ('importance', models.SmallIntegerField(choices=[(3, '重要'), (2, '一般'), (1, '次要')], default=1, verbose_name='重要程度')),
                ('title', models.CharField(max_length=120, verbose_name='标题')),
                ('detail', models.TextField(verbose_name='详细信息')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='负责人')),
            ],
        ),
    ]
