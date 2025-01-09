from django.db import models
from .choices import ChoicesCategoriaTorneio
from duelists.models import Duelist
# Create your models here.
class CategoriaTorneio(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaTorneio.choices)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.titulo   
class Torneio(models.Model):
    name = models.CharField(max_length=100)
    loja = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaTorneio, on_delete=models.CASCADE)
    duelists = models.ManyToManyField(Duelist)

    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True)
    finalizado = models.BooleanField(default=False)
    protocole = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Match(models.Model):
    tournament = models.ForeignKey(Torneio, on_delete=models.CASCADE)  # Relaciona com o torneio
    player1 = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='player1_matches')  # Jogador 1
    player2 = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='player2_matches')  # Jogador 2
    winner = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='won_matches')  # Vencedor

    def __str__(self):
        return f'{self.player1} vs {self.player2} - {self.tournament}'