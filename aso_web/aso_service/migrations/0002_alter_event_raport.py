# Generated by Django 4.0 on 2021-12-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aso_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='raport',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
