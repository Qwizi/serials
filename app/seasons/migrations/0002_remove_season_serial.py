# Generated by Django 2.2.6 on 2019-11-13 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='serial',
        ),
    ]
