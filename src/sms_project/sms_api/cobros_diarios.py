from . import models
import datetime
import time
class Gestionar_cobros():
    def procesar(ruta):
         fecha  = datetime.datetime.now()
         hora_hoy = time.strftime("%H")
         operadora,pais = ruta.split('_')
         query_pais_operadora = models.Pais_operadora.objects.filter(id_operadora__operadora=operadora,
                                                      id_pais__codigo_pais=pais)
         prueba = query_pais_operadora[0].id_pais_operadora
         #query_conexion = models.Configuracion_conexion_tigohn.objects.filter(club__id_club = id_club)
         dicdias={'MONDAY':'lunes','TUESDAY':'martes','WEDNESDAY':'miercoles','THURSDAY':'jueves', \
'FRIDAY':'viernes','SATURDAY':'sabado','SUNDAY':'domingo'}
         dia_semana = dicdias[fecha.strftime('%A').upper()]
         #query_conexion = models.Configuracion_conexion_tigohn.objects.filter(club__id_club = id_club)
         flag = 0
         if dia_semana == 'lunes':
             query_conf_envio = models.Configuracion_envio.objects.filter(lunes = True,hora_envio__hour = hora_hoy,estado=True)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'martes':
             query_conf_envio = models.Configuracion_envio.objects.filter(martes = True,hora_envio__hour = hora_hoy,estado=True)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'miercoles':
             query_conf_envio = models.Configuracion_envio.objects.filter(miercoles = True,hora_envio__hour = hora_hoy,estado=True)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'jueves':
             query_conf_envio = models.Configuracion_envio.objects.filter(jueves = True,hora_envio__hour = hora_hoy,estado=True)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'viernes':
             query_conf_envio = models.Configuracion_envio.objects.filter(viernes = True,hora_envio__hour = hora_hoy,estado=True)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'sabado':
             query_conf_envio = models.Configuracion_envio.objects.filter(sabado = True,hora_envio__hour = hora_hoy,estado=True)
             if query_conf_envio.exists():
                 flag = 1
         elif dia_semana == 'domingo':
             query_conf_envio = models.Configuracion_envio.objects.filter(domingo = True,hora_envio__hour = hora_hoy,estado=True)
             if query_conf_envio.exists():
                 flag = 1
         #id_clubs = ''
         if flag == 1:
            query_club_activos = models.Club.objects.filter(id_club__in = query_conf_envio,estado=True)
            """for recorrer in query_club_activos:
                id_clubs = id_clubs + str(recorrer.id_club) + ','
            id_clubs2 = id_clubs.strip(',')"""
            if query_club_activos.exists():

                prueba2 = 1


         return prueba
