# Generated by Django 3.0.8 on 2020-07-15 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_visit_date_visit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='user_resgister',
            new_name='user_register',
        ),
    ]