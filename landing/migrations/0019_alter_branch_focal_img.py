# Generated by Django 3.2.6 on 2021-10-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0018_branch_focal_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='focal_img',
            field=models.ImageField(default='/downlogo.PNG', upload_to='focalperson'),
        ),
    ]
