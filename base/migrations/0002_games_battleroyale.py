# Generated by Django 5.0.4 on 2024-04-27 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='BattleRoyale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_of_gameplay', models.CharField(blank=True, max_length=150, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('player_id', models.CharField(blank=True, max_length=50, null=True)),
                ('Level', models.IntegerField()),
                ('Rank', models.CharField(max_length=150)),
                ('kd_ratio', models.FloatField()),
                ('headshot_rate', models.FloatField()),
                ('no_of_headshots', models.IntegerField()),
                ('top_3_ratio', models.FloatField()),
                ('Avg_damage', models.FloatField()),
                ('Game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.games')),
            ],
        ),
    ]
