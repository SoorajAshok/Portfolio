# Generated by Django 5.0.3 on 2024-03-22 01:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_about_job_date_of_joining'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='currentStatus',
        ),
        migrations.AddField(
            model_name='about',
            name='current_status',
            field=models.CharField(choices=[('Student', 'Student'), ('Working', 'Working'), ('Freelance', 'Freelance'), ('Looking for Opportunity', 'Looking for Opportunity')], default='Looking for Opportunity', max_length=50),
        ),
        migrations.AlterField(
            model_name='about',
            name='status',
            field=models.CharField(choices=[('OTW', 'OpenToWork'), ('CW', 'CurrentlyWorking')], default='OpenToWork', max_length=30),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_of_joining',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
