# Generated by Django 2.2.6 on 2019-11-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0002_remove_season_serial'),
        ('serials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='seasons',
            field=models.ManyToManyField(to='seasons.Season'),
        ),
    ]