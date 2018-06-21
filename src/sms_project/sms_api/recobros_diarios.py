from . import models
class Gestionar_cobros():
    def procesar(self):
        fecha  = datetime.datetime.now()
        #query_conexion = models.Configuracion_conexion_tigohn.objects.filter(club__id_club = id_club)
        dicdias={'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', \
'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}
        return str(dicdias[fecha.strftime('%A').upper()])
