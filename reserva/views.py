# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template import loader

from .forms import ReservaForm

from .models import Reserva

# Create your views here.

@login_required
def nueva_reserva_view(request):
    if request.POST:
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success( request, 'Reserva creada correctamente.' )
    reservas = Reserva.objects.all()
    form = ReservaForm()
    return render(request, 'reserva/nueva_reserva.html', {
        'form'   : form,
        'reserva': reservas,
        })
