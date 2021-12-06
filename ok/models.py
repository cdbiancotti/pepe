from django.db import models

# Create your models here.

class Perro(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Soy {self.nombre}'  