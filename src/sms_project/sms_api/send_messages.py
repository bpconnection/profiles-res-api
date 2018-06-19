from rest_framework.response import Response
from . import models
import urllib

class Envio():
    def enviar(self):

        url = 'http://72.55.181.60/digicel/sms/pruebamt.php?origen=50211111111'
        #url = "http://www.google.com/"
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        urlp = response.read()

        query_corto_envio = models.Club.objects.filter(id_club = 1)

        #query_corto_envio = models.Club.objects.filter(id_club__exact=1)
        """if self.tipo_corto == 'mt_gratis':
            corto = query_corto_envio[0].corto_mt_gratis
        if self.tipo_corto == 'mt_cobro1':
            corto = query_corto_envio[0].corto_mt_cobro1
        if self.tipo_corto == 'mt_cobro2':
            corto = query_corto_envio[0].corto_mt_cobro2
        if self.tipo_corto == 'mt_cobro3':
            corto = query_corto_envio[0].corto_mt_cobro3"""

        #return "prueba:"+ str(query_corto_envio[0].corto_mt_gratis)
        return "prueba:" + str(urlp)

    def __init__(self, tipo_corto, destino, mensaje, codigo_club):
        self.tipo_corto = tipo_corto
        self.destino = destino
        self.mensaje = mensaje.lower()
        self.codigo_club = codigo_club
