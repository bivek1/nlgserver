# Generated by Django 3.1.6 on 2021-12-01 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0023_setting_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo/'),
            preserve_default=False,
        ),
    ]
