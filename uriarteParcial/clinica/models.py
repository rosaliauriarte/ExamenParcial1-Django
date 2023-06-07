from django.db import models

from users.models import usuario

# Create your models here.


#creacion de modelo para gestionar los tipo de documentos
class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "tipo_documento"
        # ordering = ["completed"]

#creacion de modelo para identificar el tipo de seguro     
class tipoSeguro(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "tipo_Seguro"
        # ordering = ["completed"]

#creacion de modelo para gestionar medicos que pertencen en la clinica       
class Doctores(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


    class Meta:
        db_table = "doctores"
        # ordering = ["completed"]

#creacion de modelo para adminitrar las especialidades de cada medico segun areas
class Especialidades(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "especialidades"
        # ordering = ["completed"]

class Paciente(models.Model):
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE,null=True,blank=True)
    nDocumento = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=150,null=True)
    fechaNacimiento = models.DateField()
    tiposeguro = models.ForeignKey(tipoSeguro, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tipodocumento+ '-' +self.nombres+ '-' +self.apellidos

    class Meta:
        db_table = "paciente"
        # ordering = ["completed"]


#creacion de modelo para gestion de citas de los pacientes      
class Citas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,null=True,blank=True)
    observaciones = models.TextField(null=True, blank=True)
    fechaCita = models.DateField()
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(usuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.paciente
    
    class Meta:
        db_table = "citas"
        # ordering = ["completed"]
