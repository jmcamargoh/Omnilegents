import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Libro

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


def import_csv(request): #hay errores en los que no sabemos por que no manda
    books = []
    with open ("books1.csv", "r") as csv_file:
        data = list(csv.reader(csv_file, delimiter=","))
        for row in data [1:]:
            books.append(
                Libro(
                    isbn13=row[5],
                    titulo=row[1],
                    autores=row[2],
                    num_pages=[7],
                    fecha_publicacion=[10],
                    editorial=[11]
                )
            )
    if len(books) > 0:
        Libro.objects.create(books)
    
    return HttpResponse("Esta guevonada importó")

#Pendiente: Login, se trabajará mas adelante