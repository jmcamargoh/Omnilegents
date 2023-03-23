from django import forms
from .models import Nota, Recordatorio

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo_nota', 'contenido_nota']

class RecordatorioForm(forms.ModelForm):
    class Meta:
        model = Recordatorio
        fields = ['mensaje','hora','metaDiaria']