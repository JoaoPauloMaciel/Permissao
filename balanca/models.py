from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

#from django.conf.urls import url, include
#from rest_framework import routers, serializers, viewsets


class Pesagem(models.Model):
    peso = models.FloatField(null=False)
    data = models.DateTimeField('date da pesagem', default=timezone.now)
    usuario = models.ForeignKey(User ,null=True, related_name='pesos')
    #usuario = models.ForeignKey('auth.User', related_name='pesos', on_delete=models.CASCADE, null=True)

class Mensagem(models.Model):
    conteudo = models.CharField(max_length=400)
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #votes = models.IntegerField(default=0)
