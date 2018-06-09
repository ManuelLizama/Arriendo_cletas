from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^nueva_reserva/$', views.nueva_reserva_view, name='nueva_reserva'),
]