# Generated by Django 3.0.8 on 2020-07-10 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visit', '0002_visit_date_visit'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_resgister', models.IntegerField(default=0)),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visit.Visit')),
            ],
        ),
    ]