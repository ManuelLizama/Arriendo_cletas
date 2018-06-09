from django import forms
from .models import Reserva


class ReservaForm ( forms.ModelForm ):
    """
        Formulario de reserva
    """

    # nombre            = forms.CharField( required = True, label = "Nombre", widget = forms.TextInput( attrs = {"class" : "form-control"} ) )

    class Meta:
        model  = Reserva
        fields = '__all__'