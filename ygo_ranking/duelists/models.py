from django.db import models

# Create your models here.
class Duelist(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, default="No Nickname")
    email = models.CharField(max_length=50)
    cossyId = models.CharField(max_length=12)
    victories = models.IntegerField(default=0)
    defeates = models.IntegerField(default=0)
    contact_number = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.name
    
class Deck(models.Model):
    deck = models.CharField(max_length=50)
    ydkcode = models.CharField(max_length=300)
    year = models.IntegerField()
    owner = models.ForeignKey(Duelist, on_delete=models.CASCADE)
    tournament_played = models.IntegerField(default=0)
    tournament_won = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return super().__str__()