# Generated by Django 3.1.6 on 2021-12-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0027_auto_20211202_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='icons',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
