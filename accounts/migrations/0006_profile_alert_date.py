# Generated by Django 2.0.5 on 2018-06-03 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_alert'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='alert_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
