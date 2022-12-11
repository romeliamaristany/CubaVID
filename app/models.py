from django.db import models

# Create your models here.

opciones_sexo = [
    [0, "Masculino"],
    [1, "Femenino"]
]
class HC(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    CI = models.CharField(max_length=11)
    edad = models.IntegerField()
    sexo = models.IntegerField(choices=opciones_sexo)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.apellidos
        
class TV(models.Model):
    HC = models.ForeignKey(HC, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=30)
    municipio_residencia = models.CharField(max_length=50)
    edad = models.IntegerField()
    lote_primera_dosis = models.CharField(max_length=10)
    fecha_primera_dosis  = models.DateField()
    hora_primera_dosis  = models.TimeField()
    enfermera_primera_dosis  = models.CharField(max_length=50)
    lote_segunda_dosis = models.CharField(max_length=10)
    fecha_segunda_dosis = models.DateField()
    hora_segunda_dosis = models.TimeField()
    enfermera_segunda_dosis = models.CharField(max_length=50)
    lote_tercera_dosis = models.CharField(max_length=10) 
    fecha_tercera_dosis = models.DateField()
    hora_tercera_dosis = models.TimeField()
    enfermera_tercera_dosis = models.CharField(max_length=50)

    
    def __str__(self):
        return self.apellidos
    
