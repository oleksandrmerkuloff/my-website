# Generated by Django 5.1.3 on 2025-01-06 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_project_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
