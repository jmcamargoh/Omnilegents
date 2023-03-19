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