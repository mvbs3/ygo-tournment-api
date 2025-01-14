from django.shortcuts import render, redirect
from django.http import HttpResponse    
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib import messages
from duelists.models import Duelist, Deck
import json
from django.core import serializers

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('<script>alert("Username já cadastrado");window.location.href = "/usuarios/cadastro/";</script>')
        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse('<script>alert("Email ja cadastrado");window.location.href = "/usuarios/cadastro/";</script>') 
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('<script>alert("Cadastrado com sucesso");window.location.href = "/";</script>') 

    
def login(request):
    if not request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'login.html')
        if request.method == "POST":
            username = request.POST.get('username')
            senha = request.POST.get('senha')
            user = authenticate(username=username, password=senha)
            if user:
                login_django(request, user)
                #funcao q so funciona quando usuarios esta autenticado: request.user.is_authenticated
                #messages.success(request, 'Logado com sucesso')()

                return redirect('landing_page')
            else:
                return HttpResponse('<script>alert("Senha inválida");window.location.href = "/usuarios/login/";</script>')

    else:
        return redirect('plataforma')
            
def plataforma(request):
    if request.user.is_authenticated:
        return HttpResponse("Logado")
    else:
        return redirect('login')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('landing_page')
    else:
        return redirect('landing_page')

def meu_perfil(request):
    if request.user.is_authenticated:
        user = request.user
        email = user.email
        duelist = Duelist.objects.filter(email=email)
        decks =  Deck.objects.filter(owner=duelist[0])
        decks_Json = json.loads(serializers.serialize("json", decks))
        decks_Json = [{'id':deck['pk'], 'fields':deck['fields']} for deck in decks_Json]
  

        if duelist.exists():
            duelist = duelist.first()
            return render(request, 'meu_perfil.html', {'duelist': duelist, 'decks': decks_Json,})
        else:
            return render(request, 'meu_perfil.html' , {'duelist': None})
        