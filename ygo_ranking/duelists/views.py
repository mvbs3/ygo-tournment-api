from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Duelist, Deck
import re
from django.core import serializers
import json
# Create your views here.
def duelists(request: object) -> HttpResponse:
    
    if request.method == "GET":
        duelists = Duelist.objects.all()
        return render(request, 'duelists.html', {'duelists': duelists})
    elif request.method == "POST":
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        cossyId = request.POST.get('cossyId')
        contact_number = request.POST.get('contact_number')
        #nao vou usar isso agora mas achei interessante
        deck =  request.POST.getlist('deck')
        ydkcode = request.POST.getlist('ydkcode')
        year = request.POST.getlist('year')
        
        #checar se o cliente ja existe
        duelist = Duelist.objects.filter(cossyId=cossyId)
        if duelist.exists():
            return HttpResponse("CossyId ja cadastrado")

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return render(request, 'duelists.html', {'name': name, 'nickname': nickname, 'cossyId': cossyId, 'contact_number': contact_number, 'decks': zip(deck, ydkcode,year), 'error': 'Email invalido'})
        if not re.match(r'^\d{2}9\d{8}$', contact_number):
            return render(request, 'duelists.html', {'name': name, 'nickname': nickname, 'cossyId': cossyId, 'email': email, 'error': 'Telefone invalido'})
        if not re.match(r'^\d{10}$', cossyId):
            return render(request, 'duelists.html', {'name': name, 'nickname': nickname, 'email': email, 'contact_number': contact_number, 'error': 'CossyId invalido'})
        
        duelist = Duelist(name=name, nickname=nickname, email=email, cossyId=cossyId, contact_number=contact_number)
        duelist.save()

        for deck, ydkcode, year in zip(deck, ydkcode, year):
            deck = Deck(deck=deck, ydkcode=ydkcode, year=year, owner=duelist)
            deck.save()

        print(name, nickname, email, cossyId, contact_number)
        return HttpResponse("Dados enviados com sucesso")

def update_duelist(request):
    id_duelist = request.POST.get('id_duelist')
    #utilizando filter no lugar de get, para nao dar erro se o id nao existir
    #acho que isso pode ser melhorado, mas o que eu fiz foi deixo por enquanto
    duelist = Duelist.objects.filter(id=id_duelist)
    #era possivel utiliza o id_duelist, mas é bom utilizar o duelist pois temos certeza q é um objeto encontrado    
    decks =  Deck.objects.filter(owner=duelist[0])
    duelist_Json = json.loads(serializers.serialize("json", duelist))[0]['fields']
    print(duelist_Json)
    decks_Json = json.loads(serializers.serialize("json", decks))
    decks_Json = [{'id':deck['pk'], 'fields':deck['fields']} for deck in decks_Json]
    print(decks_Json)
    data = {
        'duelist': duelist_Json,
        'decks': decks_Json}
    return JsonResponse (data)