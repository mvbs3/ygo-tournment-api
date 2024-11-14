from django.shortcuts import render, redirect
from .forms import PlayerForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def criar_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo produto no banco de dados
            return redirect('lista_players')
    else:
        form = PlayerForm()
    return render(request, 'torneios/criar_player.html', {'form': form})
# Create your views here.


def editar_produto(request, id):
    player = get_object_or_404(player, id=id)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'torneios/editar_player.html', {'form': form})

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o registro
            return redirect('criar_player')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})