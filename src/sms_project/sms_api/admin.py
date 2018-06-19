from django.contrib import admin

from . import models

# Register your models here.

class Pais_operadoraAdmin(admin.ModelAdmin):
    list_display = ["id_pais_operadora","id_pais", "id_operadora"]
    class Meta:
        model = models.Pais_operadora
        fields = "__all__"

class Tipo_accion(admin.ModelAdmin):
    list_display = ["tipo_accion"]
    class Meta:
        model = models.Tipo_accion
        fields = "__all__"

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ["club"]
    class Meta:
        model = models.Keywords
        fields = "__all__"

class ClubAdmin(admin.ModelAdmin):
    list_display = ["id_club","nombre_club", "pais_operadora","corto_club"]
    class Meta:
        model = models.Club
        fields = "__all__"

class Mensajes_informativoAdmin(admin.ModelAdmin):
    list_display = ["club","mensaje","tipo_accion"]
    class Meta:
        model = models.Mensajes_informativo
        fields = "__all__"

class ContenidoAdmin(admin.ModelAdmin):
    list_display = ["id_contenido","club","contenido", "aleatorio"]
    class Meta:
        model = models.Contenido
        fields = "__all__"

class Contenido_programadoAdmin(admin.ModelAdmin):
    list_display = ["contenido","estado_envio","fecha_envio", "hora_envio"]
    class Meta:
        model = models.Contenido_programado
        fields = "__all__"

class Envio_contenidoAdmin(admin.ModelAdmin):
    list_display = ["id_envio_contenido","contenido_programado","fecha"]
    class Meta:
        model = models.Envio_contenido
        fields = "__all__"

class Mensajes_moAdmin(admin.ModelAdmin):
    list_display = ["id_mo","origen","destino","mensaje","fecha"]
    class Meta:
        model = models.Mensajes_mo
        fields = "__all__"

class Club_suscriptorAdmin(admin.ModelAdmin):
    list_display = ["club","suscriptor"]
    class Meta:
        model = models.Club_suscriptor
        fields = "__all__"

class AltaAdmin(admin.ModelAdmin):
    list_display = ["club_suscriptor","fecha"]
    class Meta:
        model = models.Alta
        fields = "__all__"

class BajaAdmin(admin.ModelAdmin):
    list_display = ["club_suscriptor","fecha"]
    class Meta:
        model = models.Alta
        fields = "__all__"

admin.site.register(models.Pais)
admin.site.register(models.Operadora)
admin.site.register(models.Pais_operadora,Pais_operadoraAdmin)
admin.site.register(models.Keywords,KeywordsAdmin)
admin.site.register(models.Plataforma_envio)
admin.site.register(models.Club,ClubAdmin)
admin.site.register(models.Mensajes_informativo,Mensajes_informativoAdmin)
admin.site.register(models.Tipo_envio)
admin.site.register(models.Tipo_accion)
admin.site.register(models.Estado_envio)
admin.site.register(models.Configuracion_reenvio)
admin.site.register(models.Lista_negra)
admin.site.register(models.Contenido,ContenidoAdmin)
admin.site.register(models.Contenido_programado,Contenido_programadoAdmin)
admin.site.register(models.Envio_contenido,Envio_contenidoAdmin)
admin.site.register(models.Club_suscriptor,Club_suscriptorAdmin)
admin.site.register(models.Suscriptor)
admin.site.register(models.Configuracion_broadcast)
admin.site.register(models.Base_cargada_broadcast)
admin.site.register(models.Alta,AltaAdmin)
admin.site.register(models.Baja,BajaAdmin)
admin.site.register(models.Edge)
admin.site.register(models.Mensajes_mo,Mensajes_moAdmin)
admin.site.register(models.Dlr)
admin.site.register(models.Conteo_recobro)
admin.site.register(models.Reporte_alta)
admin.site.register(models.Reporte_baja)
admin.site.register(models.Reporte_cobro)
admin.site.register(models.Reporte_cobros_acumulado)
admin.site.register(models.Reporte_base_total)
admin.site.register(models.Reporte_refund)
