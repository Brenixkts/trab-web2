from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

def index(estado):
     return render(estado ,"diretorio/index.html")
def nordeste(estado):
      return render(estado ,"diretorio/nordeste.html")     