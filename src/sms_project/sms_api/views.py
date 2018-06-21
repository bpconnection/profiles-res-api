from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers
from . import models
from . import management_mo
from . import cobros_diarios
from . import recobros_diarios

# Create your views here.
class Sms_moApiView(APIView):

    def get(self, request, *args, **kwargs):
        origen=request.GET['origen']
        destino=request.GET['destino']
        mensaje=request.GET['mensaje']
        binfo=request.GET['binfo']
        ruta=request.GET['ruta']
        medio=request.GET['medio']
        campania=request.GET['campania']

        sms_mo = models.Mensajes_mo(
            origen=origen,
            destino=destino,
            mensaje=mensaje,
            binfo=binfo,
            ruta=ruta
        )

        sms_mo.save()
        manejo_mo = management_mo.Gestionar_mo(origen,destino,mensaje,ruta,medio,campania)
        a = manejo_mo.procesar()
        return Response({'message':'listo!!!','message2':a})

class CobrosApiView(APIView):
    def get(self, request, *args, **kwargs):
        usuario = request.GET['usuario']
        password = request.GET['password']
        ruta = request.GET['ruta'].lower()
        if usuario == 'people' and password == 'p30pl3':
            ejecutar = cobros_diarios.Gestionar_cobros.procesar(ruta)
            return Response({'message':'listo!!!','message2':ejecutar})

class RecobrosApiView(APIView):
    def get(self, request, *args, **kwargs):
        usuario = request.GET['usuario']
        password = request.GET['password']
        ruta = request.GET['ruta'].lower()
        if usuario == 'people' and password == 'p30pl3':

            ejecutar = recobros_diarios.Gestionar_recobros.procesar(ruta)
            return Response({'message':'listo!!!','message2':ejecutar})
