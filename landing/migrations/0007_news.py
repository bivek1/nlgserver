# Generated by Django 3.1.6 on 2021-05-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('files', models.FileField(upload_to='News/')),
            ],
        ),
    ]
