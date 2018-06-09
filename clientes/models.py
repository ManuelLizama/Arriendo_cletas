# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    nombre          = models.CharField( max_length = 50 )
    telefono        = models.CharField( max_length = 20, null = True, blank = True)
    correo          = models.CharField( max_length = 25, null =True, blank = True)
    activo          = models.BooleanField(default = True)
    fecha_creacion  = models.DateTimeField( auto_now_add = True, blank=True )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    # def __unicode__(self):
    #     return self.nombre
