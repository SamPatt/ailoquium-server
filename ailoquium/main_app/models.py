from django.db import models

# Create your models here.
class Score(models.Model):
    username = models.CharField(max_length=100)
    level_completed = models.IntegerField()
    energy_used = models.IntegerField()
    
    def __str__(self):
        return self.username