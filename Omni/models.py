from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_Usuario=models.IntegerField(primary_key=True)
    nombre_usuario=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    domicilio=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()

    #def __str__(self):
        #return self.id_Usuario

