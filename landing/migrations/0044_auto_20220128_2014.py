# Generated by Django 3.1.6 on 2022-01-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0043_auto_20220127_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='lience_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
