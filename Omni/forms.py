from django import forms
from .models import Nota, Recordatorio, Lib_User,Libro, Review

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo_nota', 'contenido_nota']

class RecordatorioForm(forms.ModelForm):
    class Meta:
        model = Recordatorio
        fields = ['mensaje','hora','metaDiaria']

class cambiarPagLeidasForm(forms.ModelForm):
    class Meta:
        model = Lib_User
        fields = ['pagleidas']

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtén el usuario logueado
        super().__init__(*args, **kwargs)
        self.fields['libuser_ID'].queryset = Lib_User.objects.filter(usuario=user)

    class Meta:
        model = Review
        fields = ['libuser_ID','contenido_review']