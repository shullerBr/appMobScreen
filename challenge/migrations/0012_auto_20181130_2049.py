# Generated by Django 2.0.9 on 2018-11-30 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0011_challenge_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]