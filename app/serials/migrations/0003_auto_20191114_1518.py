# Generated by Django 2.2.7 on 2019-11-14 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serials', '0002_serial_seasons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serial',
            name='premiere_date',
            field=models.CharField(max_length=128),
        ),
    ]
