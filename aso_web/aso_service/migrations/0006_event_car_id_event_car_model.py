# Generated by Django 4.0 on 2021-12-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso_service', '0005_remove_event_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='car_id',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='event',
            name='car_model',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]