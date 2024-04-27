from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    field = (
        ('player','player'),
        ('sponsor','sponsor')
    )
    option = models.CharField(max_length=100,null=True,choices=field)

    def __str__(self):
        return self.username




class Games(models.Model):
    name = models.CharField(max_length=150)
    def _str_(self):
        return self.name
    
class BattleRoyale(models.Model):
    Game = models.ForeignKey(Games, on_delete=models.CASCADE)
    Type_of_gameplay = models.CharField( max_length=150,null=True,blank=True)
    name = models.CharField(max_length=150,null=True,blank=True)
    player_id = models.CharField(max_length=50,null=True,blank=True)
    Level = models.IntegerField()
    Rank = models.CharField(max_length=150)
    kd_ratio = models.FloatField()
    headshot_rate = models.FloatField()
    no_of_headshots = models.IntegerField()
    top_3_ratio = models.FloatField()
    Avg_damage = models.FloatField()
    def _str_(self):
        return self.player_id
class ClashRoyale(models.Model):
    Game = models.ForeignKey(Games, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=True,blank=True)
    player_id = models.CharField(max_length=50,null=True,blank=True)
    Level = models.IntegerField()
    Rank = models.CharField(max_length=150)
    kd_ratio = models.FloatField()
    headshot_rate = models.FloatField()
    def __self__(self):
        return self.player_id