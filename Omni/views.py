from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario

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

def registrarUsuario(request):
    id_Usuario=request.POST['numIdUsuario']
    nombre_usuario=request.POST['txtNombreUs']
    correo=request.POST['txtCorreoUs']
    password=request.POST['txtPassword']
    domicilio=request.POST['txtDomicilio']
    fecha_nacimiento=request.POST['dateNacimiento']

    usuario=Usuario.objects.create(id_Usuario=id_Usuario, nombre_usuario=nombre_usuario, correo=correo, password=password, domicilio=domicilio, fecha_nacimiento=fecha_nacimiento)

    return redirect ('/')

#Pendiente: Login, se trabajará mas adelante