# Generated by Django 4.0 on 2022-01-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso_service', '0008_alter_event_machanic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('X', 'In Progress'), ('V', 'Complete')], default='X', max_length=20),
        ),
    ]