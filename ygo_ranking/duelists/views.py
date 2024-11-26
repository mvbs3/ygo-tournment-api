from django.shortcuts import render
from django.http import HttpResponse
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
        
        print(name, nickname, email, cossyId, contact_number)
        return HttpResponse("Dados enviados com sucesso")
