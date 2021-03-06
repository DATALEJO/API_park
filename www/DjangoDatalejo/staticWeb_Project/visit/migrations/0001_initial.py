# Generated by Django 3.0.8 on 2020-07-10 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_hour', models.TimeField()),
                ('exit_hour', models.TimeField()),
                ('allowed', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_resgister', models.IntegerField(default=0)),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.Visitor')),
            ],
        ),
    ]
