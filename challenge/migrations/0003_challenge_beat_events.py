# Generated by Django 2.0.9 on 2018-11-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_challenge_points_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='beat_events',
            field=models.IntegerField(default=0),
        ),
    ]