# Generated by Django 4.0 on 2022-01-20 17:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('describe', models.CharField(max_length=256)),
                ('time', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Position', max_length=20)),
                ('start_time', models.TimeField(default=datetime.time(6, 0))),
                ('now_time', models.TimeField(default=models.TimeField(default=datetime.time(6, 0)))),
                ('hour_time', models.TimeField(default=datetime.timedelta(seconds=3600))),
                ('end_time', models.TimeField(default=datetime.time(18, 0))),
            ],
        ),
        migrations.CreateModel(
            name='EventBooker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_end', models.TimeField(blank=True, null=True)),
                ('duration_time', models.IntegerField(default=0)),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='aso_service.station')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=15)),
                ('car_model', models.CharField(choices=[('X', 'Unknown'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'), ('A6', 'A6'), ('A7', 'A7'), ('80', '80'), ('90', '90'), ('100', '100'), ('200', '200')], default='X', max_length=15)),
                ('raport', models.CharField(blank=True, max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('In Progress', 'In Progress'), ('Complete', 'Complete')], default='Draft', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('event_booker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aso_service.eventbooker')),
                ('mechanic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.mechanic')),
                ('services', models.ManyToManyField(to='aso_service.Service')),
            ],
        ),
    ]
