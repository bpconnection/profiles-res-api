
from rest_framework.response import Response
from . import models
from . import send_messages
import datetime
import time
#from datetime import datetime, date, time, timedelta

class Gestionar_mo():

    def alta(relacion_club_suscriptor, medio, campania):
        fecha_hoy  = datetime.datetime.now()
        actualizar_club_suscriptor = relacion_club_suscriptor
        actualizar_club_suscriptor.estado = True
        actualizar_club_suscriptor.fecha_alta = fecha_hoy
        actualizar_club_suscriptor.save()

        agregar_alta =  models.Alta(
            club_suscriptor = relacion_club_suscriptor,
               medio = medio,
            campania = campania
        )
        objeto_alta = agregar_alta.save()

    def baja(relacion_club_suscriptor, medio):
        fecha_hoy  = datetime.datetime.now()
        actualizar_club_suscriptor = relacion_club_suscriptor
        actualizar_club_suscriptor.estado = False
        actualizar_club_suscriptor.fecha_baja = fecha_hoy
        actualizar_club_suscriptor.save()

        agregar_baja =  models.Baja(
            club_suscriptor = relacion_club_suscriptor,
               medio = medio
        )
        objeto_baja = agregar_baja.save()

    def mensaje_info(id_club, nombre_accion):
        query_mensajes_info = models.Mensajes_informativo.objects.filter(club__id_club=id_club,tipo_accion__nombre_accion=nombre_accion)
        return query_mensajes_info[0].mensaje

    def contenido_aleatorio(id_club):
        query_contenido_aleatorio = models.Contenido.objects.filter(club__id_club=id_club,aleatorio=True).order_by('?')[:1]
        return query_contenido_aleatorio

    def contenido_programado(id_club):
        fecha_hoy  = datetime.datetime.now()
        hora_hoy = datetime.datetime.now()

        query_contenido_programado = models.Contenido_programado.objects.filter(contenido__club__id_club=id_club,fecha_envio=fecha_hoy,hora_envio__lte=hora_hoy).order_by('?')[:1]
        if not query_contenido_programado.exists():
            query_contenido_aleatorio = Gestionar_mo.contenido_aleatorio(id_club)
            query_estado_envio = models.Estado_envio.objects.filter(estado='finalizado')
            agregar_contenido_programado = models.Contenido_programado(
                contenido = query_contenido_aleatorio[0],
                estado_envio = query_estado_envio[0],
                fecha_envio = fecha_hoy,
                hora_envio = hora_hoy,
                fecha_ejecucion=fecha_hoy,
                fecha_culminacion=fecha_hoy
            )
            agregar_contenido_programado.save()
            query_contenido_programado = agregar_contenido_programado

        return query_contenido_programado

    def procesar(self):

        operadora,pais = self.ruta.split('_')

        query_pais_operadora = models.Pais_operadora.objects.filter(id_operadora__operadora=operadora,
                                                     id_pais__codigo_pais=pais)

        mensaje = self.mensaje
        msisdn = self.origen

        query_keywords = models.Keywords.objects.filter(kw__exact=mensaje,club__pais_operadora__id_pais_operadora=query_pais_operadora[0].id_pais_operadora)

        id_club = query_keywords[0].club.id_club
        #Verifica si la keyword de alta existe

        key_valida = 0
        if query_keywords[0].tipo_accion.nombre_accion=="alta":
            key_valida = 1
            query_suscriptor = models.Suscriptor.objects.filter(msisdn=self.origen)
            if not query_suscriptor.exists():
               agregar_suscriptor =  models.Suscriptor(msisdn=self.origen)
               objeto_suscriptor = agregar_suscriptor.save()

               agregar_club_suscriptor = models.Club_suscriptor(
                    club = query_keywords[0].club,
                    suscriptor = agregar_suscriptor,
                    estado = True
               )
               agregar_club_suscriptor.save()
               Gestionar_mo.alta(agregar_club_suscriptor,self.medio,self.campania)
               msj_inf = Gestionar_mo.mensaje_info(id_club, "alta")
               id_contenido,msj_inf = Gestionar_mo.contenido_aleatorio(id_club)
            else:
                query_club_suscriptor = models.Club_suscriptor.objects.filter(suscriptor__msisdn=self.origen,club__id_club=query_keywords[0].club.id_club)
                if query_club_suscriptor.exists():
                    if query_club_suscriptor[0].estado == True:
                        msj_inf = Gestionar_mo.mensaje_info(id_club, "si_suscrito")
                        msj_inf = send_messages.Envio.enviar('mt_gratis',msisdn,msj_inf,id_club,self.ruta)
                    else:
                        Gestionar_mo.alta(query_club_suscriptor[0],self.medio,self.campania)
                        msj_inf = Gestionar_mo.mensaje_info(id_club, "re_alta")
                        contenido_programado =  management_mo.Gestionar_mo.contenido_programado(id_club)
                        resp = send_messages.Envio.enviar_contenido('mt_cobro1',msisdn,contenido_programado,id_club,self.ruta)
                else:
                    nuevo_suscriptor = models.Suscriptor.objects.filter(msisdn=self.origen)
                    agregar_club_suscriptor = models.Club_suscriptor(
                        club = query_keywords[0].club,
                        suscriptor = nuevo_suscriptor[0],
                        estado = True
                    )
                    agregar_club_suscriptor.save()
                    Gestionar_mo.alta(agregar_club_suscriptor,self.medio,self.campania)
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "alta")
                    contenido_programado =  management_mo.Gestionar_mo.contenido_programado(id_club)
                    resp = send_messages.Envio.enviar_contenido('mt_cobro1',msisdn,contenido_programado,id_club,self.ruta)

        if query_keywords[0].tipo_accion.nombre_accion=="baja":
            key_valida = 1
            query_suscriptor = models.Suscriptor.objects.filter(msisdn=self.origen)
            if not query_suscriptor.exists():
                msj_inf = Gestionar_mo.mensaje_info(id_club, "ayuda")
                msj_inf = send_messages.Envio.enviar('mt_gratis',msisdn,msj_inf,id_club,self.ruta)
            else:
                query_club_suscriptor = models.Club_suscriptor.objects.filter(suscriptor__msisdn=self.origen,club__id_club=query_keywords[0].club.id_club)
                if query_club_suscriptor.exists():
                    Gestionar_mo.baja(query_club_suscriptor[0],self.medio)
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "baja")
                    msj_inf = send_messages.Envio.enviar('mt_gratis',msisdn,msj_inf,id_club,self.ruta)
                else:
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "ayuda")
                    msj_inf = send_messages.Envio.enviar('mt_gratis',msisdn,msj_inf,id_club,self.ruta)
        if query_keywords[0].tipo_accion.nombre_accion=="ayuda":
            key_valida = 1
            query_suscriptor = models.Suscriptor.objects.filter(msisdn=self.origen)
            if not query_suscriptor.exists():
                msj_inf = Gestionar_mo.mensaje_info(id_club, "no_suscrito")
                msj_inf = send_messages.Envio.enviar('mt_gratis',msisdn,msj_inf,id_club,self.ruta)
            else:
                query_club_suscriptor = models.Club_suscriptor.objects.filter(suscriptor__msisdn=self.origen,club__id_club=query_keywords[0].club.id_club)
                if query_club_suscriptor.exists():
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "si_suscrito")
                    msj_inf = send_messages.Envio.enviar('mt_gratis',msisdn,msj_inf,id_club,self.ruta)
                else:
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "ayuda")
                    msj_inf = send_messages.Envio.enviar('mt_gratis',msisdn,msj_inf,id_club,self.ruta)

        if key_valida == 0:
            msj_inf = Gestionar_mo.mensaje_info(id_club, "key_no_valida")
            msj_inf = send_messages.Envio.enviar('mt_gratis',msisdn,msj_inf,id_club,self.ruta)


        return 'procesado!!!' + str(query_keywords[0].club.id_club) + " mensaje: "  + str(msj_inf)



    def __init__(self, origen, destino, mensaje, ruta, medio, campania):
        self.origen = origen
        self.destino = destino
        self.mensaje = mensaje.lower()
        self.ruta = ruta.lower()
        self.medio = medio.lower()
        self.campania = campania.lower()
