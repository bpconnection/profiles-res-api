from rest_framework.response import Response
from . import models

class Gestionar_reiniciar_cobros():
    def procesar():
        q = models.Club_suscriptor.objects.filter(cantidad_cobro_diario__gt=0).update(cantidad_cobro_diario=0)
        return "cobros a 0 realizado"
