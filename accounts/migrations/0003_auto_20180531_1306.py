# Generated by Django 2.0.5 on 2018-05-31 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180531_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='images'),
        ),
    ]
