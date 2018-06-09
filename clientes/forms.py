from django import forms
from .models import Cliente


class ClienteForm ( forms.ModelForm ):
    """
        Formulario de Cliente
    """
    # foto = forms.ImageField()
    # nombre            = forms.CharField( required = True, label = "Nombre", widget = forms.TextInput( attrs = {"class" : "form-control"} ) )

    class Meta:
        model  = Cliente
        fields = '__all__'
