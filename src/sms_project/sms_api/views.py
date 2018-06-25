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
from . import reiniciar_cobros
from . import captura_dlr_tigo_hn

# Create your views here.
class Sms_moApiView(APIView):

    def get(self, request, *args, **kwargs):
        origen=request.GET['origen']
        destino=request.GET['destino']
        mensaje=request.GET['mensaje']
        binfo=request.GET['binfo']
        ruta=request.GET['ruta']
        medio="sms"
        campania="sms"

        sms_mo = models.Mensajes_mo(
            origen=origen,
            destino=destino,
            mensaje=mensaje,
            binfo=binfo,
            ruta=ruta
        )

        sms_mo.save()
        manejo_mo = management_mo.Gestionar_mo(origen,destino,mensaje,binfo,ruta,medio,campania)
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

class Reiniciar_cobrosApiView(APIView):
    def get(self, request, *args, **kwargs):
        usuario = request.GET['usuario']
        password = request.GET['password']
        if usuario == 'people' and password == 'p30pl3':
            ejecutar = reiniciar_cobros.Gestionar_reiniciar_cobros.procesar()
            return Response({'message':'listo!!!','message2':ejecutar})

class Captura_dlr_tigo_hnApiView(APIView):
    def get(self, request, *args, **kwargs):
        smsc_id=request.GET['smsc-id']
        status=request.GET['status']
        answer=request.GET['answer']
        dlr_to=request.GET['to']
        dlr_from=request.GET['from']
        dlr_ts=request.GET['ts']
        id_envio=request.GET['id_envio']

        ejecutar = captura_dlr_tigo_hn.Gestionar_captura_dlr_tigo_hn.procesar(smsc_id,status,answer,dlr_to,dlr_from,dlr_ts,id_envio)
        return Response({'message':'listo!!!','message2':ejecutar})
