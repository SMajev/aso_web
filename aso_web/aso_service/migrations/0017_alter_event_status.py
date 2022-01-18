# Generated by Django 4.0 on 2022-01-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso_service', '0016_alter_event_ttd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('In Progress', 'X'), ('Complete', 'V')], default='In Progress', max_length=20),
        ),
    ]
