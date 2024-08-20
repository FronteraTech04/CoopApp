from django.db import models
from simple_history.models import HistoricalRecords
from app.core.base.models import BaseModel
from app.core.common.models import Persona
# Create your models here.



class Socio(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True, related_name='Persona')
    codigo_socio =models.CharField(max_length=20, unique=True)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'
        db_table = 'Socios'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'
    

    def desactivar(self):
        self.state = False
        self.save()


# class FirmaSocio(BaseModel):
#     firmado_por = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True, related_name='Socio')
#     firma = models.ImageField(upload_to='socios/firmas/', null=True, blank=True)
#     fecha_eliminacion = models.DateTimeField()
#     historical = HistoricalRecords()

#     class Meta:
#         verbose_name = 'Firma'
#         verbose_name_plural = 'Firmas'
#         db_table = 'Firmas_Socio'
#         ordering = ['id']

#     def __str__(self):
#         return f'{self.id}'
    

#     def desactivar(self):
#         self.state = False
#         self.save()