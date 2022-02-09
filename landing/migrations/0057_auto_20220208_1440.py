# Generated by Django 3.1.6 on 2022-02-08 08:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0056_agent_agent_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_code',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='issue_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bod',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='bod',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='bod',
            name='phone',
            field=models.BigIntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='bod',
            name='post',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bod',
            name='type',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='name',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='managementteam',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='managementteam',
            name='post',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='surveryor',
            name='area',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='surveryor',
            name='contact',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='surveryor',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='surveryor',
            name='lience_no',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='surveryor',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='surveryor',
            name='specilization',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]