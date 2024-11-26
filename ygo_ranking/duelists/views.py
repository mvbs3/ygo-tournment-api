from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def duelists(request):
    return HttpResponse('Estou em cliente')