from django.shortcuts import render

# Create your views here.
def novo_torneio(request):
    return render(request, 'novo_torneio.html')