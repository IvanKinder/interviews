# Generated by Django 3.1.3 on 2021-06-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210624_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название задачи'),
        ),
    ]
