from django.shortcuts import render
from .forms import FormTorneio
# Create your views here.
def novo_torneio(request):
    meu_form = FormTorneio()
    return render(request, 'novo_torneio.html', {'form':meu_form})