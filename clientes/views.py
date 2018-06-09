# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClienteForm
from clientes.models import Cliente
# Create your views here.
@login_required
def nuevo_cliente_view(request):
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid():
            foto = request.POST.get('foto')
            cl = form.save()
            cl.foto = foto
            cl.save()
            messages.success( request, 'Cliente creado correctamente.' )
    clientes = Cliente.objects.all()
    form = ClienteForm()
    return render(request, 'clientes/nuevo_cliente.html', {
        'form' : form,
        'clientes' : clientes,
        })


@login_required
def lista_cliente( request ):
    clientes = Cliente.objects.all()
    return render(
        request,
        'clientes/lista_clientes.html',
        {
            'clientes' : clientes
        }
    )
