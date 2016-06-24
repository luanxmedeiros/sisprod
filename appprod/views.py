from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import *

# Create your views here.

def home(request):
    return render(request,"home.html")

def listarmateria(request):
    materias=MateriaPrima.objects.all().order_by('descricao')
    lista={'materias':materias}
    return render(request,'materias.html',lista)

def listarprestadores(request):
    prestadores=Prestador.objects.all().order_by('nome')
    lista={'prestadores':prestadores}
    return render(request,'prestadores.html',lista)
