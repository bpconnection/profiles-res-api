from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers
from . import models
from . import management_mo

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
