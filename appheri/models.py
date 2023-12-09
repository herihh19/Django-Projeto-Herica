from django.db import models
from django.contrib.auth.models import User



class Usuario(User):
    nome = models.CharField(max_length=255)
    datanascimento = models.DateField()
    telefone = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255) 
