# Generated by Django 5.0.3 on 2024-03-22 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_remove_about_currentstatus_about_current_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobDescription',
            field=models.CharField(default='Job Description', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobSummary',
            field=models.CharField(default='Job Summary', max_length=800),
        ),
    ]
