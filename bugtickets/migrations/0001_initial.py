# Generated by Django 2.0.5 on 2018-06-09 02:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BugTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today, null=True)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('bug_type', models.CharField(choices=[('Functional', 'Functional'), ('Communication', 'Communication'), ('Syntax', 'Syntax'), ('Error Notices', 'Error Notices'), ('Calculation Errors', 'Calculation Errors'), ('Flow Problems', 'Flow Problems')], max_length=30)),
                ('description', models.TextField(null=True)),
                ('votes', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bugs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BugUpvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('vote_type', models.CharField(max_length=10)),
                ('bug_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug_votes', to='bugtickets.BugTicket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_author', to=settings.AUTH_USER_MODEL)),
                ('bug_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bugtickets.BugTicket')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='bugupvote',
            unique_together={('bug_ticket', 'user', 'vote_type')},
        ),
    ]
