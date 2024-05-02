from django.db import models

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=50)
    
    class Meta:
        db_table = "proyecto_regi"
        verbose_name = "proyecto_regi"
        verbose_name_plural = "proyectos_regi"
        
class Contaduria(models.Model):
    id_contaduria = models.IntegerField(primary_key=True)
    numero_escritura = models.IntegerField()
    nombre_proyecto = models.CharField(max_length=50)
    valor_registro = models.IntegerField()
    valor_deposito = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        db_table = "contaduria_regi"
        verbose_name = "contaduria_regi"
        verbose_name_plural = "contadurias_regi"