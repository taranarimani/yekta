# Generated by Django 2.2 on 2020-11-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlShorteners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(blank=True, unique=True),
        ),
    ]
