from django.db import models

# Create your models here.
class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=20, unique=True)
    codigo_pais= models.CharField(max_length=3)
    codigo_area = models.CharField(max_length=3)
    moneda = models.CharField(max_length=3)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.pais


class Operadora(models.Model):
    id_operadora =  models.AutoField(primary_key=True)
    operadora = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.operadora

class Pais_operadora(models.Model):
    id_pais_operadora =  models.AutoField(primary_key=True)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    id_operadora = models.ForeignKey(Operadora, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Pais_operadora"
        verbose_name_plural = "Pais-Operadora"
    def __str__(self):
        return '%s %s' % (self.id_pais, self.id_operadora)

class Club(models.Model):
    id_club =  models.AutoField(primary_key=True)
    nombre_club = models.CharField(max_length=20)
    pais_operadora = models.ForeignKey(Pais_operadora, on_delete=models.CASCADE)
    corto_club = models.CharField(max_length=6)
    corto_mo_gratis =  models.CharField(max_length=6)
    corto_mt_gratis = models.CharField(max_length=6)
    corto_mo_cobro = models.CharField(max_length=6)
    corto_mt_cobro1 = models.CharField(max_length=6)
    corto_mt_cobro2 = models.CharField(max_length=6)
    corto_mt_cobro3 = models.CharField(max_length=6)
    corto_broadcast = models.CharField(max_length=6)
    limite_envios_broadcast = models.PositiveIntegerField()
    cantidad_cobros_diarios = models.PositiveSmallIntegerField()
    puntos =  models.PositiveIntegerField(default=0)
    estado =  models.BooleanField()
    def __str__(self):
        return '%s %s' % (self.nombre_club, self.pais_operadora)

class Tipo_accion(models.Model):
    nombre_accion = models.CharField(max_length=50,primary_key=True)
    def __str__(self):
        return self.nombre_accion


class Keywords(models.Model):
    club= models.ForeignKey(Club,on_delete=models.CASCADE)
    kw= models.CharField(max_length=100)
    tipo_accion= models.ForeignKey(Tipo_accion,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Keywords"
        verbose_name_plural = "Keywords"


class Mensajes_informativo(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=160)
    tipo_accion = models.ForeignKey(Tipo_accion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Mensajes_informativo"
        verbose_name_plural = "Mensajes Informativos"

class Tipo_envio(models.Model):
    id_tipo_envio = models.AutoField(primary_key=True)
    tipo_envio = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Tipo_envio"
        verbose_name_plural = "Tipo Envios"
    def __str__(self):
        return self.tipo_envio

class Estado_envio(models.Model):
    id_estado_envio  = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Estado_envio"
        verbose_name_plural = "Estado Envios"
    def __str__(self):
        return self.estado

class Configuracion_envio(models.Model):
    id_configuracion_envio = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    hora_envio = models.TimeField()
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()
    fecha_ultimo_envio = models.DateTimeField(blank=True, null=True)
    estado = models.BooleanField()
    class Meta:
        verbose_name = "Configuracion_envio"
        verbose_name_plural = "Configuración Envios"

class Configuracion_reenvio(models.Model):
    id_configuracion_reenvio = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    hora_envio = models.TimeField()
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()
    fecha_ultimo_envio = models.DateTimeField(blank=True, null=True)
    estado = models.BooleanField()
    class Meta:
        verbose_name = "Configuracion_reenvio"
        verbose_name_plural = "Configuración Reenvios"

class Lista_negra(models.Model):
    id_lista_negra =  models.AutoField(primary_key=True)
    msisdn = models.CharField(max_length=11, unique=True)
    fecha = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Lista_negra"
        verbose_name_plural = "Lista Negra"

class Contenido(models.Model):
    id_contenido =  models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    aleatorio = models.BooleanField()
    def __str__(self):
        return self.texto

class Contenido_programado(models.Model):
    id_contenido_programado =  models.AutoField(primary_key=True)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    estado_envio = models.ForeignKey(Estado_envio, on_delete=models.CASCADE)
    fecha_envio = models.DateField()
    hora_envio = models.TimeField()
    fecha_ejecucion= models.DateTimeField(blank=True, null=True)
    fecha_culminacion= models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = "Contenido_programado"
        verbose_name_plural = "Contenidos Programados"
    def __str__(self):
        return format(self.id_contenido_programado)

class Envio_contenido(models.Model):
    id_envio_contenido =  models.AutoField(primary_key=True)
    id_envio = models.CharField(max_length=10,blank=True)
    cobro = models.PositiveSmallIntegerField(default=0)
    msisdn = models.CharField(max_length=11)
    contenido_programado = models.ForeignKey(Contenido_programado, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    corto = models.CharField(max_length=11)
    recobro = models.PositiveSmallIntegerField()
    class Meta:
        verbose_name = "Envio_contenido"
        verbose_name_plural = "Envio Contenidos"

class Suscriptor(models.Model):
    id_suscriptor = models.AutoField(primary_key=True)
    msisdn = models.CharField(max_length=11, unique=True)
    puntos = models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"
    def __str__(self):
        return self.msisdn


class Club_suscriptor(models.Model):
    id_club_suscriptor =  models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    suscriptor =  models.ForeignKey(Suscriptor,on_delete=models.CASCADE)
    fecha_primera_alta = models.DateTimeField(auto_now_add=True)
    fecha_alta = models.DateTimeField(blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    fecha_ultimo_evento = models.DateTimeField(auto_now=True )
    fecha_ultimo_cobro = models.DateTimeField(blank=True, null=True)
    cantidad_cobro_diario = models.PositiveIntegerField(default=0)
    estado = models.BooleanField()
    class Meta:
        verbose_name = "Club_suscriptor"
        verbose_name_plural = "Club Suscriptores"
    def __str__(self):
        return '%s %s %s %s' % (self.club,self.suscriptor,format(self.fecha_ultimo_evento),self.estado)

class Alta(models.Model):
    id_alta =  models.AutoField(primary_key=True)
    club_suscriptor = models.ForeignKey(Club_suscriptor, on_delete=models.CASCADE,null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    medio = models.CharField(max_length=20,default='sms')
    campania = models.CharField(max_length=20)
    def __str__(self):
        return format(self.fecha)

class Baja(models.Model):
    id_baja =  models.AutoField(primary_key=True)
    club_suscriptor = models.ForeignKey(Club_suscriptor, on_delete=models.CASCADE,null=True)
    fecha =  models.DateTimeField(auto_now_add=True)
    medio = models.CharField(max_length=20,default='sms')
    def __str__(self):
        return format(self.fecha)

class Configuracion_broadcast(models.Model):
    id_broadcast = models.AutoField(primary_key=True)
    id_club =  models.ForeignKey(Club, on_delete=models.CASCADE)
    corto_envio = models.CharField(max_length=6)
    fecha_envio = models.DateField()
    hora_envio = models.TimeField()
    id_tipo_envio = models.ForeignKey(Tipo_envio, on_delete=models.CASCADE)
    id_estado_envio = models.ForeignKey(Estado_envio, on_delete=models.CASCADE)
    texto = models.CharField(max_length=160)
    fecha_carga = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Configuracion_broadcast"
        verbose_name_plural = "Configuración Broadcast"

class Base_cargada_broadcast(models.Model):
    id_base_cargada = models.AutoField(primary_key=True)
    id_broadcast =  models.ForeignKey(Configuracion_broadcast, on_delete=models.CASCADE)
    msisdn = models.CharField(max_length=11)
    id_estado_envio = models.ForeignKey(Estado_envio, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    class Meta:
        verbose_name = "Base_cargada_broadcast"
        verbose_name_plural = "Base Cargada Broadcast"

class Configuracion_conexion_tigohn(models.Model):
    id_conf =  models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    host = models.CharField(max_length=50)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    dlr_mask = models.CharField(max_length=5)
    priority_c = models.CharField(max_length=2)
    priority_r = models.CharField(max_length=2)
    smsc = models.CharField(max_length=20)
    dlr_url = models.CharField(max_length=200)
    binfo = models.CharField(max_length=5)
    binfo_c = models.CharField(max_length=5)
    binfo_r = models.CharField(max_length=5)

    class Meta:
        verbose_name = "Configuracion_conexion_tigohn"
        verbose_name_plural = "Configuracion conexion tigohn"

class Mensajes_mo(models.Model):
    id_mo =  models.AutoField(primary_key=True)
    origen = models.CharField(max_length=11)
    destino = models.CharField(max_length=11)
    mensaje = models.CharField(max_length=200)
    binfo = models.CharField(max_length=6)
    ruta = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Mensajes_mo"
        verbose_name_plural = "Mensajes Entrantes"

class Dlr_tigo_hn(models.Model):
    id_dlr =  models.AutoField(primary_key=True)
    smsc_id = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    answer = models.CharField(max_length=20)
    dlr_to = models.CharField(max_length=100)
    dlr_from = models.CharField(max_length=100)
    dlr_ts = models.CharField(max_length=100)
    id_envio = models.CharField(max_length=50)
    fecha =  models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Dlr"
        verbose_name_plural = "Dlrs"

class Conteo_recobro(models.Model):
    id_conteo_recobro =  models.AutoField(primary_key=True)
    id_club = models.PositiveSmallIntegerField()
    recobro = models.PositiveSmallIntegerField(default=0)
    fecha =  models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Conteo_recobro"
        verbose_name_plural = "Conteo Recobros"

class Reporte_alta(models.Model):
    club =  models.CharField(max_length=20)
    cantidad = models.IntegerField()
    medio = models.CharField(max_length=20)
    campania = models.CharField(max_length=20)
    fecha = models.DateField()
    class Meta:
        verbose_name = "Reporte_alta"
        verbose_name_plural = "Reporte Altas"

class Reporte_baja(models.Model):
    club =  models.CharField(max_length=20)
    cantidad = models.IntegerField()
    medio = models.CharField(max_length=20)
    fecha = models.DateField()
    class Meta:
        verbose_name = "Reporte_baja"
        verbose_name_plural = "Reporte Bajas"

class Reporte_cobro(models.Model):
    club =  models.CharField(max_length=20)
    pais =  models.CharField(max_length=20)
    corto = models.CharField(max_length=11)
    medio = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    total = models.FloatField()
    fecha = models.DateField()
    class Meta:
        verbose_name = "Reporte_cobro"
        verbose_name_plural = "Reporte Cobros"


class Reporte_cobros_acumulado(models.Model):
    club =  models.CharField(max_length=20)
    pais =  models.CharField(max_length=20)
    corto = models.CharField(max_length=11)
    medio = models.CharField(max_length=20)
    cantidad = models.IntegerField()
    total = models.FloatField()
    mes = models.CharField(max_length=2)
    anio = models.CharField(max_length=4)
    class Meta:
        verbose_name = "Reporte_cobros_acumulado"
        verbose_name_plural = "Reporte Cobros Acumulados"

class Reporte_base_total(models.Model):
    club =  models.CharField(max_length=20)
    pais =  models.CharField(max_length=20)
    operadora =  models.CharField(max_length=15)
    usuarios_activos = models.IntegerField()
    usuarios_baja = models.IntegerField()
    fecha = models.DateField()
    class Meta:
        verbose_name = "Reporte_base_total"
        verbose_name_plural = "Reporte Base Total"

class Reporte_refund(models.Model):
    club =  models.CharField(max_length=20)
    pais =  models.CharField(max_length=20)
    corto = models.CharField(max_length=11)
    operadora = models.CharField(max_length=15)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    class Meta:
        verbose_name = "Reporte_refund"
        verbose_name_plural = "Reporte Refunds"
