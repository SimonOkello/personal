# Generated by Django 3.0.5 on 2020-04-14 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jionyeshe', '0002_auto_20200414_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
    ]
