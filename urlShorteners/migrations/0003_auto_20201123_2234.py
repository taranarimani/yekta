# Generated by Django 2.2 on 2020-11-23 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlShorteners', '0002_auto_20201123_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(blank=True),
        ),
    ]
