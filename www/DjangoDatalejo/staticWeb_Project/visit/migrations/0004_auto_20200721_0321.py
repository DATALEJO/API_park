# Generated by Django 3.0.8 on 2020-07-21 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0003_auto_20200715_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='exit_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='user_register',
            field=models.IntegerField(default=0, null=True),
        ),
    ]