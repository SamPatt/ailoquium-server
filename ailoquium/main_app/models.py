from django.db import models

class Score(models.Model):
    username = models.CharField(max_length=100)
    level = models.IntegerField()
    time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class TotalScore(models.Model):
    username = models.CharField(max_length=100)
    highest_level = models.IntegerField()
    total_time = models.IntegerField()
    total_money = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username