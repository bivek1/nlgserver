# Generated by Django 3.1.6 on 2021-12-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0025_auto_20211202_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='sub_product',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]