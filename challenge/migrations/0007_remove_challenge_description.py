# Generated by Django 2.0.9 on 2018-11-30 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0006_auto_20181130_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='description',
        ),
    ]
