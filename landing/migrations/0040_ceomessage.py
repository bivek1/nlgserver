# Generated by Django 3.1.6 on 2022-01-25 10:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0039_setting_product_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeoMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
