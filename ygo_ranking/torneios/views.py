from django.shortcuts import render, redirect
from .forms import PlayerForm
from django.shortcuts import get_object_or_404


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