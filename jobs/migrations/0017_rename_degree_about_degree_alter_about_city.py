# Generated by Django 5.0.3 on 2024-04-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_about_degree_about_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='Degree',
            new_name='degree',
        ),
        migrations.AlterField(
            model_name='about',
            name='city',
            field=models.CharField(default='Saint John, New Brunswick, Canada', max_length=200),
        ),
    ]