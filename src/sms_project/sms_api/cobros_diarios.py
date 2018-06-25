from . import models
import datetime
import time
from . import management_mo
from . import send_messages

class Gestionar_cobros():
    def conteo_recobro(id_club):
        query_actualizar_conteo = models.Conteo_recobro.objects.filter(id_club=id_club)
        if query_actualizar_conteo.exists():
            actualizar_conteo = query_actualizar_conteo[0]
            actualizar_conteo.recobro = query_actualizar_conteo[0].recobro + 1
            actualizar_conteo.save()
        else:
            agregar_conteo_recobro =  models.Conteo_recobro(
                id_club = id_club
            )
            objeto_conteo_recobro = agregar_conteo_recobro.save()

    def actualizar_fecha_envio(id_club,hora_hoy):
        fecha_hoy  = datetime.datetime.now()
        query_actualizar_fecha = models.Configuracion_envio.objects.filter(club__id_club=id_club,hora_envio__hour = hora_hoy)
        if query_actualizar_fecha.exists():
            actualizar_fecha_envio = query_actualizar_fecha[0]
            actualizar_fecha_envio.fecha_ultimo_envio = fecha_hoy
            actualizar_fecha_envio.save()

    def procesar(ruta):
         fecha_hoy  = datetime.datetime.now()
         hora_hoy = time.strftime("%H")
         operadora,pais = ruta.split('_')
         query_pais_operadora = models.Pais_operadora.objects.filter(id_operadora__operadora=operadora,
                                                      id_pais__codigo_pais=pais)
         pais_operadora = query_pais_operadora[0].id_pais_operadora

         dicdias={'MONDAY':'lunes','TUESDAY':'martes','WEDNESDAY':'miercoles','THURSDAY':'jueves','FRIDAY':'viernes','SATURDAY':'sabado','SUNDAY':'domingo'}
         dia_semana = dicdias[fecha_hoy.strftime('%A').upper()]

         flag = 0
         if dia_semana == 'lunes':
             query_conf_envio = models.Configuracion_envio.objects.filter(lunes = True,hora_envio__hour = hora_hoy,estado=True,club__pais_operadora__id_pais_operadora = pais_operadora)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'martes':
             query_conf_envio = models.Configuracion_envio.objects.filter(martes = True,hora_envio__hour = hora_hoy,estado=True,club__pais_operadora__id_pais_operadora = pais_operadora)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'miercoles':
             query_conf_envio = models.Configuracion_envio.objects.filter(miercoles = True,hora_envio__hour = hora_hoy,estado=True,club__pais_operadora__id_pais_operadora = pais_operadora)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'jueves':
             query_conf_envio = models.Configuracion_envio.objects.filter(jueves = True,hora_envio__hour = hora_hoy,estado=True,club__pais_operadora__id_pais_operadora = pais_operadora)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'viernes':
             query_conf_envio = models.Configuracion_envio.objects.filter(viernes = True,hora_envio__hour = hora_hoy,estado=True,club__pais_operadora__id_pais_operadora = pais_operadora)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'sabado':
             query_conf_envio = models.Configuracion_envio.objects.filter(sabado = True,hora_envio__hour = hora_hoy,estado=True,club__pais_operadora__id_pais_operadora = pais_operadora)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'domingo':
             query_conf_envio = models.Configuracion_envio.objects.filter(domingo = True,hora_envio__hour = hora_hoy,estado=True,club__pais_operadora__id_pais_operadora = pais_operadora)
             if query_conf_envio.exists():
                 flag = 1
         resp = ""
         if flag == 1:
            query_club_activos = models.Club.objects.filter(id_club__in = query_conf_envio,estado=True,pais_operadora__id_pais_operadora = pais_operadora)

            if query_club_activos.exists():
                for recorrer_club in query_club_activos:
                    Gestionar_cobros.conteo_recobro(recorrer_club.id_club)
                    Gestionar_cobros.actualizar_fecha_envio(recorrer_club.id_club,hora_hoy)
                    query_suscriptor_activos = models.Club_suscriptor.objects.filter(club__id_club = recorrer_club.id_club,estado=True,fecha_alta__lte = fecha_hoy)
                    contenido_programado =  management_mo.Gestionar_mo.contenido_programado(recorrer_club.id_club)
                    if query_suscriptor_activos.exists():
                        for recorrer_suscritos in query_suscriptor_activos:
                            resp = send_messages.Envio.enviar_contenido('mt_cobro1',recorrer_suscritos.suscriptor.msisdn,contenido_programado,recorrer_club.id_club,ruta)
         return str(resp)
