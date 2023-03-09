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
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
        for row in csv_data:
            _, created = Libro.objects.get_or_create(
                isbn13=row[5],
                titulo=row[1],
                autores=row[2],
                num_pages=row[7],
                fecha_publicacion=row[10],
                editorial=row[11]
            )
        return render (request, 'import_csv.html', {'success':True})
    else:
        return render (request, 'import_csv.html')
    
    #return HttpResponse("Esta guevonada importó")

#Pendiente: Login, se trabajará mas adelante