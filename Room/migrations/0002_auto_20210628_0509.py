# Generated by Django 2.2.24 on 2021-06-28 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='abailavility',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='num',
            field=models.IntegerField(),
        ),
    ]
