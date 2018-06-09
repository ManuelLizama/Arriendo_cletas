# -*- coding: utf-8 -*-

from django.db import models
from clientes.models import Cliente
from django.utils import timezone

# Create your models here.
class Bicicleta(models.Model):
    nombre = models.CharField( max_length = 70, verbose_name = u'nombre', help_text = "Nombre Producto" )
    descripcion = models.CharField( blank = True, null = True, max_length = 100, verbose_name = u'descripcion', help_text = "Descripcion Producto" )
    valor = models.IntegerField( verbose_name = u'valor', help_text = "Valor del Producto" )
    activo = models.BooleanField( default = False)
    fecha_creacion = models.DateField( auto_now_add = True, blank=True )

    """docstring for Bicicleta"""
    

class Reserva(models.Model):
    cliente = models.ForeignKey( Cliente, verbose_name = u'cliente' )
    boleta = models.IntegerField( verbose_name = u'boleta', help_text = "Numero de Boleta" )
    bici = models.ForeignKey( Bicicleta, verbose_name = u'bicicleta', default = True)
    fecha_creacion = models.DateField( auto_now_add = True , blank=True)
    fecha_modificacion = models.DateField( auto_now = True , )
    


        
