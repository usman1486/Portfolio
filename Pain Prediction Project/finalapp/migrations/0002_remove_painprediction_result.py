# Generated by Django 4.1.2 on 2022-11-08 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painprediction',
            name='result',
        ),
    ]