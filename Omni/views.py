from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Usuario, Libro, Nota, Reto, Recordatorio, Lib_User

from .forms import NotaForm, RecordatorioForm
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

@login_required
def home(request):
    return render (request, 'home.html') #página inicial a donde se acceden a las opciones

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
   lib_user=Lib_User(libro_id=libro.bookID, usuario=request.user)
   lib_user.save()
   return render (request, 'home.html')


@login_required
def mislibros(request):
    return render (request, 'mislibros.html') #página de mis libros




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
# ----------------------------------------------------------------

#Manejo de los recordatorios
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
#-----------------------------------------------------------------
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