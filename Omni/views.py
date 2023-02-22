from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request, 'home.html') #página inicial a donde se acceden a las opciones

def libros(request):
    return render (request, 'libros.html') #página de libros (busqueda solamente)

def login(request):
    return render (request, 'login.html') #página del login

def mislibros(request):
    return render (request, 'mislibros.html') #página de mis libros

def registro(request):
    return render (request, 'registro.html') #página de registro

#Pendiente: Login, se trabajará mas adelante