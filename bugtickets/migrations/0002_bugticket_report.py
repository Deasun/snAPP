# Generated by Django 2.0.5 on 2018-06-09 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugticket',
            name='report',
            field=models.TextField(blank=True, null=True),
        ),
    ]
