from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    TIPO = [
        ('B', 'Básica'),
        ('P', 'Premium'),
        ('D', 'Diamante'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_de_suscripción = models.CharField(max_length=1, choices=TIPO)
    número_de_tarjeta_de_crédito = models.CharField(max_length=16)
    CVV = models.CharField(max_length=3)
    fecha_de_expiración = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.get_subscription_tier_display()}"


class CausaSocial(models.Model):
    # Lista de Objetivos de Desarrollo Sostenible (ODS) como opciones
    ODS_CHOICES = [
        ('fin_pobreza', 'Fin de la pobreza'),
        ('hambre_cero', 'Hambre cero'),
        ('salud_bienestar', 'Salud y bienestar'),
        ('educacion_calidad', 'Educación de calidad'),
        ('igualdad_genero', 'Igualdad de género'),
        ('agua_limpia', 'Agua limpia y saneamiento'),
        ('energia_asequible', 'Energía asequible y no contaminante'),
        ('trabajo_decente', 'Trabajo decente y crecimiento económico'),
        ('industria_innovacion', 'Industria, innovación e infraestructuras'),
        ('reduccion_desigualdades', 'Reducción de las desigualdades'),
        ('ciudades_sostenibles', 'Ciudades y comunidades sostenibles'),
        ('produccion_consumo', 'Producción y consumo responsables'),
        ('accion_clima', 'Acción por el clima'),
        ('vida_submarina', 'Vida submarina'),
        ('vida_terrestre', 'Vida de ecosistemas terrestres'),
        ('paz_justicia', 'Paz, justicia e instituciones sólidas'),
        ('alianzas_objetivos', 'Alianzas para lograr objetivos'),
    ]

    nombre_causa = models.CharField(max_length=255, verbose_name="Nombre de la Causa")
    ong = models.CharField(max_length=255, verbose_name="Nombre de la ONG")
    descripcion = models.TextField(verbose_name="Descripción de la Causa")
    monto_meta = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Monto Meta (CLP)")
    ods_relacionados = models.ManyToManyField('ODS', verbose_name="ODS Relacionados", related_name="causas")

    def __str__(self):
        return self.nombre_causa


class ODS(models.Model):
    # Tabla independiente para los ODS, para escalabilidad
    clave = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
