# Generated by Django 3.1.6 on 2022-02-13 17:28

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0065_auto_20220211_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]