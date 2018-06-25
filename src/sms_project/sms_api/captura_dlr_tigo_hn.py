from rest_framework.response import Response
from . import models
class Gestionar_captura_dlr_tigo_hn():
    def procesar(smsc_id,status,answer,dlr_to,dlr_from,dlr_ts,id_envio):
        guardar_dlr = models.Dlr_tigo_hn(
            smsc_id=smsc_id,
            status=status,
            answer=answer,
            dlr_to=dlr_to,
            dlr_from=dlr_from,
            dlr_ts=dlr_ts,
            id_envio=id_envio
        )

        guardar_dlr.save()

        return "Guardar DLR"
