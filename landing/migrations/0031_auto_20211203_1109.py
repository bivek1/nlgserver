# Generated by Django 3.1.6 on 2021-12-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0030_departmenthead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managementteam',
            name='appointed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='managementteam',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]