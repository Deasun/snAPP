# Generated by Django 2.0.5 on 2018-05-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180503_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='trade_union',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
