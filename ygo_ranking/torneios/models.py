from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    cossyId = models.CharField(max_length= 12)
    victories = models.IntegerField(default=0)
    defeates = models.IntegerField(default = 0)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Nome Real: {self.name}; Apelido: {self.nickname}; Cossy: {self.cossyId}"


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    modality = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)  # Relaciona com o torneio
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1_matches')  # Jogador 1
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2_matches')  # Jogador 2
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='won_matches')  # Vencedor

    def __str__(self):
        return f'{self.player1} vs {self.player2} - {self.tournament}'
