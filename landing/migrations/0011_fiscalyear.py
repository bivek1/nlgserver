# Generated by Django 3.1.6 on 2021-07-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_auto_20210712_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='fiscalYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiscal', models.CharField(max_length=200)),
            ],
        ),
    ]
