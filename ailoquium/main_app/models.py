from django.db import models

class Score(models.Model):
    username = models.CharField(max_length=100)
    level_completed = models.IntegerField()
    energy_used = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
