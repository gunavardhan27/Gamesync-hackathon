# Generated by Django 5.0.2 on 2024-04-27 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_games_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='battleroyale',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='ClashRoyale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('player_id', models.CharField(blank=True, max_length=50, null=True)),
                ('Level', models.IntegerField()),
                ('Rank', models.CharField(max_length=150)),
                ('kd_ratio', models.FloatField()),
                ('headshot_rate', models.FloatField()),
                ('Game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.games')),
            ],
        ),
    ]
