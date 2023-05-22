from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    id_Usuario=models.IntegerField(primary_key=True)
    nombre_usuario=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    domicilio=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre_usuario, self.id_Usuario)
    

class Libro(models.Model):
    bookID=models.CharField(max_length = 15,primary_key= True)
    titulo=models.CharField(max_length= 120)
    autores=models.CharField(max_length= 250)
    isbn = models.CharField(max_length = 14)
    num_pages=models.IntegerField()
    fecha_publicacion=models.CharField(max_length=15)
    editorial=models.CharField(max_length=50)
    num_calificaciones = models.IntegerField(default=0)
    calificacion_total = models.FloatField(default=0.0)
    calificacion_promedio = models.FloatField(default=0.0)
    genero = models.CharField(max_length=20,default="N/A")

    def __str__(self):
        texto = "{1} ({0})"
        return texto.format(self.titulo, self.isbn)


class Lib_User(models.Model):
    libuser_ID=models.IntegerField(primary_key=True, unique=True, null=False)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE, to_field='bookID')
    pagleidas = models.IntegerField()

    def __str__(self):
        texto = "{1} ({0}) Libro: {2}"
        return texto.format(self.libuser_ID, self.usuario, self.libro.titulo)
    
    def obtener_autores(self):
        libros = Lib_User.objects.filter(usuario=self.usuario)
        autores = []
        for libro in libros:
            autores.extend(libro.libro.autores.split(","))
        return list(set(autores))

class Nota(models.Model):
    nota_id=models.IntegerField(primary_key=True)
    id_UsuarioNota=models.ForeignKey(User, on_delete=models.CASCADE)   
    titulo_nota=models.CharField(max_length=100)
    contenido_nota=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_modificacion=models.DateTimeField(auto_now=True)

    def __str__(self):
        texto = "{1} ({0})"
        return texto.format(self.titulo_nota, self.nota_id)
    
class Reto(models.Model):
    reto_id = models.IntegerField(primary_key=True)
    #id_UsuarioNota=models.ForeignKey(Usuario, on_delete=models.CASCADE)  PENDIENTE DE REALIZARSE, DADO QUE PARA ESTA ITERACION AUN NO HAY MANEJO DE USUARIOS
    descripcion = models.CharField(max_length=100)
    tituloReto = models.CharField(max_length=20)
    estadoReto = models.BooleanField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.tituloReto, self.reto_id)
    
class Recordatorio(models.Model):
    recordatorio_id = models.IntegerField(primary_key=True)
    #id_UsuarioNota=models.ForeignKey(Usuario, on_delete=models.CASCADE)  PENDIENTE DE REALIZARSE, DADO QUE PARA ESTA ITERACION AUN NO HAY MANEJO DE USUARIOS
    mensaje = models.CharField(max_length=20)
    hora = models.CharField(max_length=10)
    metaDiaria = models.IntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.tituloReto, self.reto_id)


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    libuser_ID = models.ForeignKey(Lib_User, on_delete=models.CASCADE)
    contenido_review = models.TextField()
    fecha_review = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.review_id, self.libuser_ID)  