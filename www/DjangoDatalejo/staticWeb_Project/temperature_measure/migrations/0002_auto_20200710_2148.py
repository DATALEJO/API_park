# Generated by Django 3.0.8 on 2020-07-10 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_visit_date_visit'),
        ('temperature_measure', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TemperatureMeasure',
            new_name='Temperature_Measure',
        ),
    ]
