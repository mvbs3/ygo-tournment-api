from django.db import models
from .choices import ChoicesCategoriaTorneio
from duelists.models import Duelist
from datetime import datetime
from secrets import token_hex, token_urlsafe
from django.contrib.auth.models import User
import math
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
    duelists = models.ManyToManyField(Duelist, null=True, blank=True)

    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True)
    finalizado = models.BooleanField(default=False)
    protocolo = models.CharField(max_length=44, null=True, blank=True)
    identificador = models.CharField(max_length=24, null=True, blank=True)
    num_rodadas = models.IntegerField(default=1)
    winner = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='torneios_ganhos', null=True, blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime("%d/%m/%Y-%H:%M:%-S-") + token_hex(12)
        if not self.identificador:
            self.identificador = token_urlsafe(16)
        super().save(*args, **kwargs)
    def atualizar_ranking(self):
        matches = self.match_set.all()
        for match in matches:
            winner = match.winner
            if winner:
                winner.victories += 1
                winner.pontos += 1
                winner.save()
    def definir_num_rodadas(self):
        duelists = self.duelists.all()
        num_duelists = duelists.count()
        if num_duelists < 2:
            return 0
        num_rodadas = math.ceil(math.log2(num_duelists))
        self.num_rodadas = num_rodadas
        self.save()
        return num_rodadas
    def user_inscrito(self):
        duelist = Duelist.objects.get(email=self.request.user.email)
        return self.duelists.filter(id=duelist.id).exists()        

class Match(models.Model):
    tournament = models.ForeignKey(Torneio, on_delete=models.CASCADE)  # Relaciona com o torneio
    player1 = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='player1_matches')  # Jogador 1
    player2 = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='player2_matches')  # Jogador 2
    winner = models.ForeignKey(Duelist, on_delete=models.CASCADE, related_name='won_matches')  # Vencedor

    def __str__(self):
        return f'{self.player1} vs {self.player2} - {self.tournament}'