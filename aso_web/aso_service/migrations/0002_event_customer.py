# Generated by Django 4.0 on 2022-01-12 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('aso_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
            preserve_default=False,
        ),
    ]