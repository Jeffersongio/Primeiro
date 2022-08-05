from django.db import models


# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
