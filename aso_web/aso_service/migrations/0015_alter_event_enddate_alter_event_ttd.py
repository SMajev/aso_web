# Generated by Django 4.0 on 2022-01-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso_service', '0014_alter_event_mechanic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='ttd',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]