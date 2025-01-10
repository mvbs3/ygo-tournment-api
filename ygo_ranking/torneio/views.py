from django.shortcuts import render,get_object_or_404
from .forms import FormTorneio
from django.http import HttpResponse   
from .models import Torneio 
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
        torneios = Torneio.objects.all()
        return render(request, 'listar_torneio.html', {"torneios" : torneios})
def acessar_torneio(request,identificador):
    torneio = get_object_or_404(Torneio, identificador=identificador)
    return render(request, 'acessar_torneio.html', {"torneio" : torneio})