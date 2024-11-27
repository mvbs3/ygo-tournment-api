from django.shortcuts import render
from django.http import HttpResponse
from .models import Duelist
import re
# Create your views here.
def duelists(request: object) -> HttpResponse:
    
    if request.method == "GET":
        return render(request, 'duelists.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        cossyId = request.POST.get('cossyId')
        contact_number = request.POST.get('contact_number')
        #nao vou usar isso agora mas achei interessante
        carros =  request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')
        
        #checar se o cliente ja existe
        duelist = Duelist.objects.filter(cossyId=cossyId)
        if duelist.exists():
            return HttpResponse("CossyId ja cadastrado")

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return render(request, 'duelists.html', {'name': name, 'nickname': nickname, 'cossyId': cossyId, 'contact_number': contact_number, 'error': 'Email invalido'})
        if not re.match(r'^\d{2}9\d{8}$', contact_number):
            return render(request, 'duelists.html', {'name': name, 'nickname': nickname, 'cossyId': cossyId, 'email': email, 'error': 'Telefone invalido'})
        if not re.match(r'^\d{10}$', cossyId):
            return render(request, 'duelists.html', {'name': name, 'nickname': nickname, 'email': email, 'contact_number': contact_number, 'error': 'CossyId invalido'})
        
        duelist = Duelist(name=name, nickname=nickname, email=email, cossyId=cossyId, contact_number=contact_number)
        duelist.save()

        for carro, placa, ano in zip(carros, placas, anos):
            print(carro, placa, ano)

        print(name, nickname, email, cossyId, contact_number)
        return HttpResponse("Dados enviados com sucesso")
