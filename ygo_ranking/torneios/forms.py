from django import forms
from .models import Player, Tournament  # Substitua com o modelo correspondente

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'nickname', 'email', 'cossyId', 'contact_number']  # Defina os campos que deseja no formulário

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'date', 'modality']  # Defina os campos que deseja no formulário
