# Generated by Django 2.2.24 on 2021-06-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_remove_client_is_recruiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_recruiter',
            field=models.BooleanField(default=False),
        ),
    ]
