# Generated by Django 3.1.6 on 2021-03-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_branch_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('details', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Surveryor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('specilization', models.CharField(max_length=100, null=True)),
                ('area', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
