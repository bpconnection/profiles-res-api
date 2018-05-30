from django.contrib import admin

from . import models

# Register your models here.

class Pais_operadoraAdmin(admin.ModelAdmin):
    list_display = ["id_pais_operadora","id_pais", "id_operadora"]
    class Meta:
        model = models.Pais_operadora
        fields = "__all__"

class ClubAdmin(admin.ModelAdmin):
    list_display = ["id_club","nombre_club", "id_pais_operadora"]
    class Meta:
        model = models.Club
        fields = "__all__"

class Mensajes_informativoAdmin(admin.ModelAdmin):
    list_display = ["id_club","bienvenida1", "bienvenida2","salida","ayuda","ayuda_multiple"]
    class Meta:
        model = models.Mensajes_informativo
        fields = "__all__"

class ContenidoAdmin(admin.ModelAdmin):
    list_display = ["id_contenido","id_club","contenido", "aleatorio"]
    class Meta:
        model = models.Mensajes_informativo
        fields = "__all__"

class Contenido_programadoAdmin(admin.ModelAdmin):
    list_display = ["id_contenido","id_estado_envio","fecha_envio", "hora_envio"]
    class Meta:
        model = models.Mensajes_informativo
        fields = "__all__"

class Envio_contenidoAdmin(admin.ModelAdmin):
    list_display = ["id_envio_contenido","id_contenido_programado","fecha"]
    class Meta:
        model = models.Mensajes_informativo
        fields = "__all__"

admin.site.register(models.Pais)
admin.site.register(models.Operadora)
admin.site.register(models.Pais_operadora,Pais_operadoraAdmin)
admin.site.register(models.Plataforma_envio)
admin.site.register(models.Club,ClubAdmin)
admin.site.register(models.Mensajes_informativo,Mensajes_informativoAdmin)
admin.site.register(models.Tipo_envio)
admin.site.register(models.Estado_envio)
admin.site.register(models.Configuracion_reenvio)
admin.site.register(models.Lista_negra)
admin.site.register(models.Contenido,ContenidoAdmin)
admin.site.register(models.Contenido_programado,Contenido_programadoAdmin)
admin.site.register(models.Envio_contenido,Envio_contenidoAdmin)
admin.site.register(models.Club_suscriptor)
admin.site.register(models.Suscriptor)
admin.site.register(models.Configuracion_broadcast)
admin.site.register(models.Base_cargada_broadcast)
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
