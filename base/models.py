from django.db import models

# Create your models here.
class BattleRoyale(models.Model):
    name = models.CharField(max_length=150)
    player_id = models.CharField(max_length=50,null=True,blank=True)
    Rank = models.CharField(max_length=150)
    kd_ratio = models.FloatField()
    headshot_rate = models.FloatField()
    no_of_headshots = models.IntegerField()
    top_3_ratio = models.FloatField()
    Avg_damage = models.FloatField()
    def __str__(self):
        return self.name

    