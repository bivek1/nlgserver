# Generated by Django 3.1.6 on 2022-01-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0048_auto_20220128_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='Report/'),
        ),
        migrations.AlterField(
            model_name='download',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='Report/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]