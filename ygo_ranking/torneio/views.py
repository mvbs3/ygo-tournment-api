from django.shortcuts import render
from .forms import FormTorneio
from django.http import HttpResponse    
# Create your views here.
def novo_torneio(request):
    if request.method == "GET":
        meu_form = FormTorneio()
        return render(request, 'novo_torneio.html', {'form':meu_form})
    elif request.method == "POST":
        meu_form = FormTorneio(request.POST)
        if meu_form.is_valid():
            meu_form.save()
            return HttpResponse("Torneio criado com sucesso")
        else:
            return render(request, 'novo_torneio.html', {'form':meu_form})
def listar_torneio(request):
    if request.method == "GET":
        return render(request, 'listar_torneios.html')
    elif request.method == "POST":
        pass