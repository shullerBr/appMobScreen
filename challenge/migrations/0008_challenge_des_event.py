# Generated by Django 2.0.9 on 2018-11-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0007_remove_challenge_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='des_event',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]