# Generated by Django 4.0 on 2022-01-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso_service', '0028_rename_position_event_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='enddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]