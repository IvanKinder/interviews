# Generated by Django 3.1.3 on 2021-07-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210719_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='static', verbose_name='Картинка'),
        ),
    ]
