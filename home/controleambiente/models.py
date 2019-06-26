from django.db import models
from django.utils import timezone

    
class Local(models.Model):
    nome = models.CharField(max_length = 100, unique=True)
    status = models.CharField(max_length = 100, blank=True, default="OK")

    def __str__(self):
        return self.nome

class Ambiente(models.Model):
    temperatura = models.DecimalField(max_digits=8, decimal_places=5)
    umidade = models.DecimalField(max_digits=8, decimal_places=5)
    data = models.DateTimeField(default=timezone.now)
    local = models.ForeignKey('Local', max_length = 100, on_delete=models.CASCADE, blank=False, default=1)
    
    
    def __str__(self):
        return str(self.local.nome) + str(self.data)
