from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import *

# Create your views here.

def home(request):
    return render(request,"home.html")
