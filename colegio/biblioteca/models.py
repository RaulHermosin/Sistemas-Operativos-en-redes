from django.db import models

# Create your models here.
class libro(models.Model):
    id = models.AutoField(primary_key=True)
    libro = models.CharField(max_length=15, blank= False)
    pagina = models.CharField(max_length=20, blank= False)
