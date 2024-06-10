from django.db import models

# Create your models here.

class Servico(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    data = models.CharField(max_length=10)
    solicitante = models.CharField(max_length=50)
    contato = models.CharField(max_length=13)
    def __str__(self):
        return self.codigo
    def __str__(self):
        return self.descricao
    def __str__(self):
        return self.data
    def __str__(self):
        return self.solicitante
    def __str__(self):
        return self.contato
