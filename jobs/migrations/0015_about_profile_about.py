# Generated by Django 5.0.3 on 2024-04-05 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_remove_about_current_status_remove_about_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_about',
            field=models.CharField(default='Profile Summary', max_length=800),
        ),
    ]