# Generated by Django 5.0.3 on 2024-03-22 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_alter_job_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_of_joining',
            field=models.DateField(null=True),
        ),
    ]