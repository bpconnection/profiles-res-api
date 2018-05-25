from django.contrib import admin

from . import models

# Register your models here.


admin.site.register(models.Pais)
admin.site.register(models.Operadora)
admin.site.register(models.Pais_operadora)
admin.site.register(models.Plataforma_envio)
admin.site.register(models.Club)
admin.site.register(models.Mensajes_informativo)
admin.site.register(models.Tipo_envio)
admin.site.register(models.Estado_envio)
admin.site.register(models.Configuracion_reenvio)
admin.site.register(models.Lista_negra)
admin.site.register(models.Contenido)
admin.site.register(models.Contenido_programado)
admin.site.register(models.Envio_contenido)
admin.site.register(models.Club_suscriptor)
admin.site.register(models.Suscriptor)
admin.site.register(models.Broadcast)
admin.site.register(models.Base_cargada)
admin.site.register(models.Alta)
admin.site.register(models.Baja)
admin.site.register(models.Edge)
admin.site.register(models.Mensajes_mo)
admin.site.register(models.Dlr)
admin.site.register(models.Conteo_recobro)
admin.site.register(models.Reporte_alta)
admin.site.register(models.Reporte_baja)
admin.site.register(models.Reporte_cobro)
admin.site.register(models.Reporte_cobros_acumulado)
admin.site.register(models.Reporte_base_total)
admin.site.register(models.Reporte_refund)
