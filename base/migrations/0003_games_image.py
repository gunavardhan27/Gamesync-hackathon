# Generated by Django 5.0.4 on 2024-04-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_games_battleroyale'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
