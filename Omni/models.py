from django.db import models

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

    def __str__(self):
        texto = "{1} ({0})"
        return texto.format(self.titulo, self.isbn)


class Nota(models.Model):
    nota_id=models.IntegerField(primary_key=True)
    #id_UsuarioNota=models.ForeignKey(Usuario, on_delete=models.CASCADE)    PENDIENTE DE REALIZARSE, DADO QUE PARA ESTA ITERACION AUN NO HAY MANEJO DE USUARIOS
    titulo_nota=models.CharField(max_length=100)
    contenido_nota=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_modificacion=models.DateTimeField(auto_now=True)

    def __str__(self):
        texto = "{1} ({0})"
        return texto.format(self.titulo_nota, self.nota_id)
    
class Reto(models.Model):
    reto_id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    tituloReto = models.CharField(max_length=20)
    estadoReto = models.BooleanField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.tituloReto, self.reto_id)