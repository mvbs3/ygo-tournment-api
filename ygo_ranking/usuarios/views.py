from django.shortcuts import render, redirect
from django.http import HttpResponse    
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib import messages
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
            return HttpResponse("Username ja cadastrado")
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse("Cadastro realizado com sucesso")
    
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

                return HttpResponse("Login realizado com sucesso")
            else:
                return HttpResponse('<script>alert("Senha inválida");</script>')

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
        return redirect('login')
    else:
        return redirect('login')