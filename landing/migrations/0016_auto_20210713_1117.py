# Generated by Django 3.1.6 on 2021-07-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0015_auto_20210713_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='News/'),
        ),
    ]
