from rest_framework.response import Response
from . import models
import urllib
from time import time

class Envio():
    def uniqid(prefix = ''):
        #return prefix + hex(int(time()*10000000))[2:]
        return prefix + hex(int(time()))[2:10] + hex(int(time()*1000000) % 0x100000)[2:7]

    #def enviar_tigo_hn(tipo_corto, msisdn, id_contenido, mensaje, id_club):
    def enviar_tigo_hn(tipo_corto, msisdn, mensaje, id_club):

        query_conexion = models.Configuracion_conexion_tigohn.objects.filter(club__id_club = id_club)

        host = query_conexion[0].host
        username = query_conexion[0].username
        password = query_conexion[0].password
        dlr_mask = query_conexion[0].dlr_mask
        priority_c = query_conexion[0].priority_c
        priority_r = query_conexion[0].priority_r
        smsc = query_conexion[0].smsc
        dlr_url = query_conexion[0].dlr_url
        binfo_c = query_conexion[0].binfo_c
        binfo_r = query_conexion[0].binfo_r

        id_envio = Envio.uniqid()

        if tipo_corto == 'mt_gratis':
            corto = query_conexion[0].club.corto_mt_gratis
            binfo = binfo_r.upper()
            recobro = '0'
            priority = priority_r

        url_dlr = dlr_url + '&myid=' + id_envio + '&id_club=' + str(id_club) + '&recobro=' + recobro
        url_kannel = host + 'username=' + username + '&password=' + password + '&from=' + corto + '&to=' + str(msisdn) + '&text=' + mensaje + '&dlr-mask=' + dlr_mask + '&priority=' + priority + '&smsc=' + smsc + '&dlr-url=' + url_dlr + '&binfo=' + binfo
        """
        url = 'http://72.55.181.60/digicel/sms/pruebamt.php?origen=50211111111'
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        urlp = response.read()"""
        """if tip_corto != 'mt_gratis':
            guardar_envio_contenido = models.Envio_contenido(
                id_envio = id_envio,
                cobro = 0,
                msisdn = msisdn,
                contenido_programado = contenido_programado[0],
                corto = corto,
                recobro = 0
            )
            guardar_envio_contenido.save()"""
        return url_kannel

    def enviar_contenido_tigo_hn(tipo_corto, msisdn, contenido_programado, id_club):
        mensaje = contenido_programado[0].contenido.texto

        query_conexion = models.Configuracion_conexion_tigohn.objects.filter(club__id_club = id_club)

        host = query_conexion[0].host
        username = query_conexion[0].username
        password = query_conexion[0].password
        dlr_mask = query_conexion[0].dlr_mask
        priority_c = query_conexion[0].priority_c
        priority_r = query_conexion[0].priority_r
        smsc = query_conexion[0].smsc
        dlr_url = query_conexion[0].dlr_url
        binfo_c = query_conexion[0].binfo_c
        binfo_r = query_conexion[0].binfo_r

        id_envio = Envio.uniqid()

        if tipo_corto == 'mt_gratis':
            corto = query_conexion[0].club.corto_mt_gratis
            binfo = binfo_r.upper()
            recobro = '0'
            priority = priority_r
        if tipo_corto == 'mt_cobro1':
            corto = query_conexion[0].club.corto_mt_cobro1
            binfo = binfo_c.upper()
            recobro = '0'
            priority = priority_c
        if tipo_corto == 'mt_cobro2':
            corto = query_conexion[0].club.corto_mt_cobro2
            binfo = binfo_c.upper()
            recobro = '1'
            priority = priority_c
        if tipo_corto == 'mt_cobro3':
            corto = query_conexion[0].club.corto_mt_cobro3
            binfo = binfo_c.upper()
            recobro = '2'
            priority = priority_c

        url_dlr = dlr_url + '&myid=' + id_envio + '&id_club=' + str(id_club) + '&recobro=' + recobro
        url_kannel = host + 'username=' + username + '&password=' + password + '&from=' + corto + '&to=' + str(msisdn) + '&text=' + mensaje + '&dlr-mask=' + dlr_mask + '&priority=' + priority + '&smsc=' + smsc + '&dlr-url=' + url_dlr + '&binfo=' + binfo
        """
        url = 'http://72.55.181.60/digicel/sms/pruebamt.php?origen=50211111111'
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        urlp = response.read()"""
        if tipo_corto != 'mt_gratis':
            guardar_envio_contenido = models.Envio_contenido(
                id_envio = id_envio,
                cobro = 0,
                msisdn = msisdn,
                contenido_programado = contenido_programado[0],
                corto = corto,
                recobro = 0
            )
            guardar_envio_contenido.save()
        return url_kannel

    def enviar(tipo_corto,msisdn,mensaje,id_club,ruta):
        if ruta == 'tigo_hn':
            r = Envio.enviar_tigo_hn(tipo_corto,msisdn,mensaje,id_club)
        return "prueba:" + str(r)
    def enviar_contenido(tipo_corto,msisdn,contenido_programado,id_club,ruta):
        if ruta == 'tigo_hn':
            r = Envio.enviar_contenido_tigo_hn(tipo_corto,msisdn,contenido_programado,id_club)

        return "prueba:" + str(r)
