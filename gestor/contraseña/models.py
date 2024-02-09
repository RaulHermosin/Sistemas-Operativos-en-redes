from django.db import models

# Create your models here.
class usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=15, blank= False)
    contraseña = models.CharField(max_length=20, blank= False)
