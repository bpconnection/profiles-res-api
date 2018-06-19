
from rest_framework.response import Response
from . import models
from . import send_messages


class Gestionar_mo():

    def alta(relacion_club_suscriptor, medio, campania):
        agregar_alta =  models.Alta(
            club_suscriptor = relacion_club_suscriptor,
               medio = medio,
            campania = campania
        )
        objeto_alta = agregar_alta.save()

    def baja(relacion_club_suscriptor, medio):
        agregar_baja =  models.Baja(
            club_suscriptor = relacion_club_suscriptor,
               medio = medio
        )
        objeto_baja = agregar_baja.save()

    def mensaje_info(id_club, nombre_accion):
        query_mensajes_info = models.Mensajes_informativo.objects.filter(club__id_club__exact=id_club,tipo_accion__nombre_accion__exact=nombre_accion)
        return query_mensajes_info[0].mensaje

    def contenido_aleatorio(id_club):
        query_contenido_aleatorio = models.Contenido.objects.filter(club__id_club__exact=id_club,aleatorio__exact=True).order_by('?')[:1]
        #query_contenido_aleatorio.order_by('?')[:1]
        return query_contenido_aleatorio[0].contenido

    def procesar(self):

        """operadora,pais = self.ruta.split('_')"""
        pais = "gt"
        operadora = "claro"

        query_pais_operadora = models.Pais_operadora.objects.filter(id_operadora__operadora=operadora,
                                                     id_pais__codigo_pais=pais)

        mensaje = self.mensaje
        msisdn = self.origen

        query_keywords = models.Keywords.objects.filter(kw__exact=mensaje,club__pais_operadora__id_pais_operadora=query_pais_operadora[0].id_pais_operadora)

        id_club =  int(query_keywords[0].club.id_club)
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
               msj_inf = Gestionar_mo.contenido_aleatorio(id_club)
            else:
                query_club_suscriptor = models.Club_suscriptor.objects.filter(suscriptor__msisdn=self.origen,club__id_club=query_keywords[0].club.id_club)
                if query_club_suscriptor.exists():
                    """actualizar_club_suscriptor = query_club_suscriptor[0]
                    actualizar_club_suscriptor.estado = False
                    actualizar_club_suscriptor.save(force_update=True)"""
                    #mensaje = "mensaje Ya esta suscrito"
                    if query_club_suscriptor[0].estado == True:
                        #msj_inf = Gestionar_mo.mensaje_info(id_club, "si_suscrito")
                        a = send_messages.Envio("mt_gratis",msisdn,"prueba",1)

                        msj_inf = a.enviar()
                    else:
                        actualizar_club_suscriptor = query_club_suscriptor[0]
                        actualizar_club_suscriptor.estado = True
                        actualizar_club_suscriptor.save()
                        msj_inf = Gestionar_mo.mensaje_info(id_club, "re_alta")
                        msj_inf = Gestionar_mo.contenido_aleatorio(id_club)
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
                    msj_inf = Gestionar_mo.contenido_aleatorio(id_club)
        if query_keywords[0].tipo_accion.nombre_accion=="baja":
            key_valida = 1
            query_suscriptor = models.Suscriptor.objects.filter(msisdn=self.origen)
            if not query_suscriptor.exists():
                #mensaje = "mensaje de ayuda"
                msj_inf = Gestionar_mo.mensaje_info(id_club, "ayuda")
            else:
                query_club_suscriptor = models.Club_suscriptor.objects.filter(suscriptor__msisdn=self.origen,club__id_club=query_keywords[0].club.id_club)
                if query_club_suscriptor.exists():
                    actualizar_club_suscriptor = query_club_suscriptor[0]
                    actualizar_club_suscriptor.estado = False
                    actualizar_club_suscriptor.save()
                    Gestionar_mo.baja(actualizar_club_suscriptor,self.medio)
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "baja")
                else:
                    #mensaje = "mensaje de ayuda"
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "ayuda")

        if query_keywords[0].tipo_accion.nombre_accion=="ayuda":
            key_valida = 1
            query_suscriptor = models.Suscriptor.objects.filter(msisdn=self.origen)
            if not query_suscriptor.exists():
                #mensaje = "mensaje no esta suscrito"
                msj_inf = Gestionar_mo.mensaje_info(id_club, "no_suscrito")
            else:
                query_club_suscriptor = models.Club_suscriptor.objects.filter(suscriptor__msisdn=self.origen,club__id_club=query_keywords[0].club.id_club)
                if query_club_suscriptor.exists():
                    #mensaje = "esta suscrito al club tal"
                    #mensaje = "esta suscrito a los clubs"
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "si_suscrito")
                else:
                    #mensaje = "mensaje de ayuda"
                    msj_inf = Gestionar_mo.mensaje_info(id_club, "ayuda")

        if key_valida == 0:
            #mensaje = "mensaje no ingreso una key valida"
            msj_inf = Gestionar_mo.mensaje_info(id_club, "key_no_valida")

        envio_sms = send_messages.Envio(self.origen,self.destino,self.mensaje,self.ruta)
        a = envio_sms.enviar()
        return 'procesado!!!' + str(query_keywords[0].club.id_club) + " mensaje: "  + str(operadora) +" "+ str(pais)



    def __init__(self, origen, destino, mensaje, ruta, medio, campania):
        self.origen = origen
        self.destino = destino
        self.mensaje = mensaje.lower()
        self.ruta = ruta.lower()
        self.medio = medio.lower()
        self.campania = campania.lower()
