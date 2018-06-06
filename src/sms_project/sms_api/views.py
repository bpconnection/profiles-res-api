from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers
from . import models

# Create your views here.
class Sms_moApiView(APIView):
    def get(self, request, *args, **kwargs):
        origen=request.GET['origen']
        destino=request.GET['destino']
        mensaje=request.GET['mensaje']
        binfo=request.GET['binfo']
        ruta=request.GET['ruta']

        sms_mo = models.Mensajes_mo(
            origen=origen,
            destino=destino,
            mensaje=mensaje,
            binfo=binfo,
            ruta=ruta
        )
        sms_mo.save()
        return Response({'message':'listo!!!'})
