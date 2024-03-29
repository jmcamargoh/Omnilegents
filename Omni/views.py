from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .models import Libro, Nota, Reto, Recordatorio, Lib_User, Review

from .forms import NotaForm, RecordatorioForm, cambiarPagLeidasForm, ReviewForm
import pandas as pd


#---------------------------------------
# Poblado de la BD de libro con el Dataset 

class LibroSTR:
  def __init__(self, bookID,title, author, isbn, num_page, publication_date, publisher):
    self.bookID = bookID
    self.title = title
    self.author = author
    self.isbn = isbn
    self.num_page = num_page
    self.publication_date = publication_date
    self.publisher = publisher

  def getID(self):
     return self.bookID
  
  def getTitle(self):
    return self.title

  def getAuthor(self):
    return self.author

  def getIsbn(self):
    return self.isbn

  def getNumPage(self):
    return self.num_page
  
  def getPublicationDate(self):
    return self.publication_date
   
  def getPublisher(self):
     return self.publisher

def registradorLibros(dataframe):
  listaLibros = []
  for a in range(1,len(dataframe[0])):
    listaLibros.append(LibroSTR(str(dataframe[0][a]).strip(),str(dataframe[1][a]).strip(),str(dataframe[2][a]).strip(),str(dataframe[3][a]).strip(),str(dataframe[4][a]).strip(),str(dataframe[5][a]).strip(),str(dataframe[6][a]).strip()))
  return listaLibros

def import_csv(request): 
    if request.method == 'POST':
      csv_Name = request.POST.get('csvName')
      dfLibros = pd.read_csv(csv_Name,sep=",",header = None)
      listaLibros = registradorLibros(dfLibros)
      for lib in listaLibros:
        libro = Libro.objects.create(bookID = lib.getID(), titulo = lib.getTitle() , autores = lib.getAuthor(),isbn = lib.getIsbn() , num_pages = lib.getNumPage() , fecha_publicacion = lib.getPublicationDate( ), editorial = lib.getPublisher() ) 
      return render (request, 'import_csv.html', {'success':True})    
    else:
        return render (request, 'import_csv.html')
    return HttpResponse("Importacion exitosa")

def randomizarGeneros(request):
   generos = ("Terror", "Comedia", "Novela", "Poesia","Suspenso")
   libros = Libro.objects.all()
   longitud = len(libros)
   for a in range(0,longitud):
      r = a%5
      libros[a].genero = generos[r]
      libros[a].save()
   return render(request,'randomizarGeneros.html')

#---------------------------------------
# Página Home

@login_required
def home(request):
    return render (request, 'home.html') #página inicial a donde se acceden a las opciones

#---------------------------------------
# Búsqueda y agregación de libros

@login_required
def libros(request):
    libroBuscado = request.GET.get('searchBook')
    if libroBuscado:
       libros = Libro.objects.filter(Q(titulo=libroBuscado) | Q(isbn=libroBuscado))
    else:
       libros = Libro.objects.order_by('?')[:20]
    return render (request, 'libros.html', {'libroBuscado':libroBuscado, 'libros':libros}) #página de libros (busqueda solamente)

@login_required
def agregarLibro(request, libro_id):
   libro=Libro.objects.get(bookID=libro_id)

   if Lib_User.objects.filter(libro_id=libro.bookID, usuario=request.user).exists():
      messages.error(request, f"El libro ya se encuentra en tu Biblioteca")
   else:
      lib_user=Lib_User(libro_id=libro.bookID, usuario=request.user, pagleidas=0)
      lib_user.save()
      messages.success(request, f"El libro ha sido agregado a tu Biblioteca")
   return render (request, 'home.html')

#---------------------------------------
# Sección MisLibros
import matplotlib.pyplot as plt

@login_required
def mislibros(request):
   usuario = request.user
   libros_usuario = Lib_User.objects.filter(usuario=usuario)

   nombreUsuario = None
   if libros_usuario:
      nombreUsuario = str(libros_usuario[0].usuario.username)
   
   

   librosGrafica = []
   xAxis = []
   yAxis = []
   for a in range(0,len(libros_usuario)):
      if libros_usuario[a].pagleidas != 0 and libros_usuario[a].tiempoLeido!= 0 :
         librosGrafica.append(libros_usuario[a])
         if(len(libros_usuario[a].libro.titulo)>20):
            xAxis.append(libros_usuario[a].libro.titulo[:20])
         else: 
            xAxis.append(libros_usuario[a].libro.titulo)
         yMoment = libros_usuario[a].pagleidas / libros_usuario[a].tiempoLeido
         yAxis.append(yMoment)
   fig,ax = plt.subplots()
   ax.bar(xAxis,yAxis)
   ax.set_xlabel('Libros')
   ax.set_ylabel('Paginas Leidas por minuto')
   ax.set_title('Rendimiento de lectura')
   plt.savefig("Omni/static/GraficasMisLibros/Grafica.png")


      
      

   context = {'libros_usuario':libros_usuario}
   return render (request, 'mislibros.html', context)

@login_required
def cambiarPagLeidas(request, pk):
   LibUser = get_object_or_404(Lib_User, pk = pk)

   if request.method == 'POST':
      form = cambiarPagLeidasForm(request.POST, instance=LibUser)
      if form.is_valid():
         LibUser = form.save(commit=False)
         LibUser.usuario = request.user
         LibUser.save()
         return redirect('../../mislibros')
   else:
      form=cambiarPagLeidasForm(instance=LibUser)
   return render(request, 'cambiarPagLeidas.html', {'form':form})

@login_required
def calificar_libro(request, libro_pk):
    libro = get_object_or_404(Libro, pk=libro_pk)
    if request.method == 'POST':
        calificacion = float(request.POST['calificacion'])
        if calificacion < 1 or calificacion > 5:
            messages.error(request, 'La calificación debe estar entre 1 y 5.')
        else:
            libro.num_calificaciones += 1
            libro.calificacion_total += calificacion
            libro.calificacion_promedio = libro.calificacion_total / libro.num_calificaciones
            libro.save()
            messages.success(request, 'Libro calificado correctamente.')

    # Obtener el promedio de calificaciones actualizado
    libros_usuario = Lib_User.objects.filter(usuario=request.user)
    for libro_usuario in libros_usuario:
        libro_usuario.calificacion_promedio = libro_usuario.libro.calificacion_promedio
        libro_usuario.save()

    return redirect('mislibros')



def recomendar_libros(request):
    if request.user.is_authenticated:
        libros_usuario = Lib_User.objects.filter(usuario=request.user)
        autores = set()
        generos = set()
        
        for libro in libros_usuario:
            autores.update(libro.libro.autores.split(","))
            generos.add(libro.libro.genero)
        
        libros_recomendados_autor = []
        libros_recomendados_genero = []

        for autor in autores:
            libros = Libro.objects.filter(autores__contains=autor).exclude(bookID__in=[libro.libro.bookID for libro in libros_usuario]).order_by("-num_pages")[:5]
            libros_recomendados_autor.extend(list(libros))

        for genero in generos:
            libros = Libro.objects.filter(genero=genero).exclude(bookID__in=[libro.libro.bookID for libro in libros_usuario]).order_by("-num_pages")[:5]
            libros_recomendados_genero.extend(list(libros))

        libros_recomendados = libros_recomendados_autor + libros_recomendados_genero
        libros_recomendados = list(set(libros_recomendados))  # Eliminar duplicados
        
        context = {"libros_recomendados": libros_recomendados}
        return render(request, "recomendar_libros.html", context)
    else:
        return redirect("login")



 
#---------------------------------------
# Manejo de las notas en la aplicación

@login_required
def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
          nota = form.save(commit=False)
          nota.id_UsuarioNota = request.user
          nota.save()
          return redirect('lista_notas')
    else:
      form=NotaForm()
    return render (request, 'crear_nota.html', {'form': form})

@login_required
def editar_nota(request, pk):
   nota = get_object_or_404(Nota, pk=pk)
   if request.method == 'POST':
      form = NotaForm(request.POST, instance=nota)
      if form.is_valid():
         nota = form.save(commit=False)
         nota.id_UsuarioNota = request.user
         nota.save()
         return redirect('detalle_nota', pk=nota.pk)
   else:
      form=NotaForm(instance=nota)
   return render(request, 'editar_nota.html', {'form':form})

@login_required
def eliminar_nota(request, pk):
   nota = get_object_or_404(Nota, pk=pk)
   if nota.id_UsuarioNota == request.user:
      nota.delete()
   return redirect('lista_notas')

@login_required
def lista_notas(request):
   notas = Nota.objects.filter(id_UsuarioNota = request.user)
   return render(request, 'lista_notas.html', {'notas':notas})

@login_required
def detalle_nota(request, pk):
   nota = get_object_or_404(Nota, pk=pk)
   return render(request, 'detalle_nota.html', {'nota':nota})

#---------------------------------------
# Manejo de los recordatorios en la aplicación

@login_required
def crear_recordatorio(request):
    if request.method == 'POST':
        form = RecordatorioForm(request.POST)
        if form.is_valid():
          rec = form.save(commit=False)
          rec.save()
          return redirect('recordatorios')
    else:
      form=RecordatorioForm()
    return render (request, 'crear_recordatorio.html', {'form': form})

@login_required
def eliminar_recordatorio(request, pk):
   rec = get_object_or_404(Recordatorio, pk=pk)
   rec.delete()
   return redirect('recordatorios')

@login_required
def recordatorios(request):
  recordatorios = Recordatorio.objects.all()
  return render(request, 'recordatorios.html', {'recordatorios':recordatorios})

@login_required
def detalle_recordatorio(request, pk):
   rec = get_object_or_404(Recordatorio, pk=pk)
   return render(request, 'detalle_recordatorios.html', {'rec':rec})

#---------------------------------------
# Retos Y Logros

@login_required
def retosylogros(request):
   return render (request, 'retosylogros.html')

@login_required
def retos(request):
   retosListados = Reto.objects.all()
   return render (request,'retos.html', {'retosListados':retosListados})

@login_required
def logros(request):
  return render (request, 'logros.html')

#---------------------------------------
#  Reviews

@login_required
def leer_reviews(request):
   reviews = Review.objects.order_by('-fecha_review')
   return render(request, 'reviews.html', {'reviews':reviews})

@login_required
def crear_review(request):
   if request.method == 'POST':
      form = ReviewForm(request.POST, user=request.user)
      if form.is_valid():
         review = form.save(commit=False)
         review.save()
         return redirect('leer_reviews')
   else:
      form = ReviewForm(user=request.user)
   return render (request, 'crear_review.html', {'form': form})

@login_required
def mis_reviews(request):
   user = request.user
   reviews = Review.objects.filter(libuser_ID__usuario=user)
   return render(request, 'mis_reviews.html', {'reviews':reviews})

@login_required
def eliminar_review(request, pk):
   review = get_object_or_404(Review, pk=pk)
   review.delete()
   return redirect('leer_reviews')

@login_required
def editar_review(request, pk):
   review = get_object_or_404(Review, pk=pk)
   if request.method == 'POST':
      form = ReviewForm(request.POST, instance=review, user=request.user)
      if form.is_valid():
         review.save()
         return redirect('mis_reviews')
   else:
      form=ReviewForm(instance=review, user=request.user)
   return render(request, 'editar_review.html', {'form':form})