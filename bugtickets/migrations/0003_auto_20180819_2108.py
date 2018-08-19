# Generated by Django 2.0.5 on 2018-08-19 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugtickets', '0002_bugticket_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugticket',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_bugs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bugupvote',
            name='bug_ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bug_votes', to='bugtickets.BugTicket'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='bug_ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bugtickets.BugTicket'),
        ),
    ]
