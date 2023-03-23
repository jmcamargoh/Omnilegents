from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Usuario, Libro, Nota, Reto

from .forms import NotaForm
import pandas as pd



#---------------------------------------
 
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

#---------------------------------------



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


#---------------------------------------
# Manejo de las notas en la aplicación

def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
          nota = form.save(commit=False)
          nota.save()
          return redirect('lista_notas')
    else:
      form=NotaForm()
    return render (request, 'crear_nota.html', {'form': form})


def editar_nota(request, pk):
   nota = get_object_or_404(Nota, pk=pk)
   if request.method == 'POST':
      form = NotaForm(request.POST, instance=nota)
      if form.is_valid():
         nota = form.save(commit=False)
         nota.save()
         return redirect('detalle_nota', pk=nota.pk)
   else:
      form=NotaForm(instance=nota)
   return render(request, 'editar_nota.html', {'form':form})


def eliminar_nota(request, pk):
   nota = get_object_or_404(Nota, pk=pk)
   nota.delete()
   return redirect('lista_notas')


def lista_notas(request):
   notas = Nota.objects.all()
   return render(request, 'lista_notas.html', {'notas':notas})


def detalle_nota(request, pk):
   nota = get_object_or_404(Nota, pk=pk)
   return render(request, 'detalle_nota.html', {'nota':nota})
# ----------------------------------------------------------------

def retosylogros(request):
   return render (request, 'retosylogros.html')

def retos(request):
   retosListados = Reto.objects.all()
   return render (request,'retos.html', {'retosListados':retosListados})

def logros(request):
  return render (request, 'logros.html')