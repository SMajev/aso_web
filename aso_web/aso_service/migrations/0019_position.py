# Generated by Django 4.0 on 2022-01-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso_service', '0018_alter_event_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]