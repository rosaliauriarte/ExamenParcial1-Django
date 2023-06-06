from django.db import models
from django.contrib.auth.models import User
from users.models import Usuario

# Create your models here.
class TipoDoc(models.Model):
   tipo_documento_nombre = models.CharField(max_length=255)
   created_at = models.DateTimeField(auto_now_add=True)  
   def __str__(self):
       return self.title
  
   class Meta:
       db_table = "Tipos_Documento_identidad"

class TipoSeg(models.Model):
   tipo_seguro_nombre = models.CharField(max_length=255)
   created_at = models.DateTimeField(auto_now_add=True)  
   def __str__(self):
       return self.title
  
   class Meta:
       db_table = "tipos_seguro"

class Especialidad(models.Model):
   especialidad_nombre = models.CharField(max_length=255)
   created_at = models.DateTimeField(auto_now_add=True)  
   def __str__(self):
       return self.title
  
   class Meta:
       db_table = "especialidades"

class Doctor(models.Model):
    nombre_doctor = models.CharField(max_length=255,null=True)
    doctor_direccion = models.CharField(max_length=255)
    doctor_telefono = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
       return self.title
  
    class Meta:
       db_table = "doctores"

class Paciente(models.Model):
   nombres = models.CharField(max_length=255, null=False)
   apellidos = models.CharField(max_length=255, null=False)
   nro_documento = models.CharField(max_length=255, null=False)
   direccion = models.CharField(max_length=255, null=True)
   nacimiento = models.CharField(max_length=255, null=True)
   tipo_documento = models.ForeignKey(TipoDoc,on_delete=models.CASCADE, null=True, blank=True)
   tipo_seguro = models.ForeignKey(TipoSeg,on_delete=models.CASCADE, null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
  
   class Meta:
       db_table = "pacientes"

class Cita(models.Model):
   fecha_cita = models.DateField(null=False)
   observaciones = models.CharField(max_length=255, null=False)
   paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, null=True, blank=True)
   especialidad = models.ForeignKey(Especialidad,on_delete=models.CASCADE, null=True, blank=True)
   doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True, blank=True)
   username = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   def __str__(self):
       return self.title
  
   class Meta:
       db_table = "citas_medicas"

