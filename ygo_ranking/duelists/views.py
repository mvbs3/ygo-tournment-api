from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Duelist, Deck
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
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
            return render(request, 'duelists.html', {'name': name, 'nickname': nickname, 'cossyId': cossyId, 'email': email, 'decks': zip(deck, ydkcode,year), 'error': 'Telefone invalido'})
        if not re.match(r'^\d{10}$', cossyId):
            return render(request, 'duelists.html', {'name': name, 'nickname': nickname, 'email': email, 'decks': zip(deck, ydkcode,year),'contact_number': contact_number, 'error': 'CossyId invalido'})
        
        duelist = Duelist(name=name, nickname=nickname, email=email, cossyId=cossyId, contact_number=contact_number)
        duelist.save()

        for deck, ydkcode, year in zip(deck, ydkcode, year):
            deck = Deck(deck=deck, ydkcode=ydkcode, year=year, owner=duelist)
            deck.save()

        print(name, nickname, email, cossyId, contact_number)
        return HttpResponse("Dados enviados com sucesso")

def update_duelist(request):
    #retorna o duelista na tela (NAO ATAULIZA O VALOR)
    id_duelist = request.POST.get('id_duelist')
    #utilizando filter no lugar de get, para nao dar erro se o id nao existir
    #acho que isso pode ser melhorado, mas o que eu fiz foi deixo por enquanto
    duelist = Duelist.objects.filter(id=id_duelist)
    #era possivel utiliza o id_duelist, mas é bom utilizar o duelist pois temos certeza q é um objeto encontrado    
    decks =  Deck.objects.filter(owner=duelist[0])
    duelist_Json = json.loads(serializers.serialize("json", duelist))[0]['fields']
    duelist_id = json.loads(serializers.serialize("json", duelist))[0]['pk']
    print(duelist_Json)
    decks_Json = json.loads(serializers.serialize("json", decks))
    decks_Json = [{'id':deck['pk'], 'fields':deck['fields']} for deck in decks_Json]
    print(decks_Json)
    data = {
        'duelist': duelist_Json,
        'decks': decks_Json,
        'duelist_id': duelist_id}
    return JsonResponse (data)

@csrf_exempt
def update_deck(request, id):
    deck = Deck.objects.get(id=id)
    deck.deck = request.POST.get('deck')
    deck.ydkcode = request.POST.get('ydkcode')

    deck.year = request.POST.get('year')
    list_decks = Deck.objects.exclude(id=id).filter(ydkcode=deck.ydkcode)
    if list_decks.exists():
        return HttpResponse("Ja existe um deck com esse ydkcode")
    deck.save()
    return HttpResponse("Deck atualizado com sucesso")

def delete_deck(request, id):
    try:
        deck = Deck.objects.get(id=id)
        deck.delete()
        return redirect(reverse('duelists')+f'?aba=att_duelist&id_duelist={deck.owner.id}')
    except:
        return redirect(reverse('duelists')+f'?aba=att_duelist&id_duelist={deck.owner.id}')

def atualizar_duelist(request,id):
    body = json.loads(request.body)
    print(body['name'])
    name = body['name']
    nickname = body['nickname']
    email = body['email']
    cossyId = body['cossyId']
    contact_number = body['contact_number']
    
    #atualizar duelista
    duelist = get_object_or_404(Duelist, id=id)
    try:
        duelist.name = name     
        duelist.nickname = nickname
        duelist.email = email
        list_users = Duelist.objects.exclude(id=id).filter(email=email)
        if list_users.exists():
            return HttpResponse("Ja existe um usuario com esse email")
        duelist.cossyId = cossyId
        list_users = Duelist.objects.exclude(id=id).filter(cossyId=cossyId)
        if list_users.exists():
            return HttpResponse("Ja existe um usuario com esse cossyId")
        duelist.contact_number = contact_number
        list_users = Duelist.objects.exclude(id=id).filter(contact_number=contact_number)   
        if list_users.exists():
            return HttpResponse("Ja existe um usuario com esse telefone")
        duelist.save()


        return JsonResponse({'status': '200','name':name, 'nickname': nickname, 'email': email, 'cossyId': cossyId, 'contact_number': contact_number})
    except:
        return JsonResponse({'status': '500'})    