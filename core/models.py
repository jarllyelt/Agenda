from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(verbose_name='Data de Criação', auto_now=True)
    # Comando "DataTimeField" é para saber a data que está sendo criado o evento, e o comando "Auto_Now" para saber a hora de forma automatica que foi criado.
    # Comando "Verbose_name" Serve para customizar os nomes.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo
    #Tratar para que o nome do evento dentro do ADMIN aparece o titulo

