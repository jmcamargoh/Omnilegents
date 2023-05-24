from django.contrib import admin
from .models import Usuario, Libro, Nota, Reto, Lib_User, Review

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Nota)
admin.site.register(Reto)
admin.site.register(Lib_User)
admin.site.register(Review)