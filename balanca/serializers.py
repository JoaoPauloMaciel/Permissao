from django.contrib.auth.models import User, Group
from balanca.models import Pesagem, Mensagem
from rest_framework import serializers

class PesosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pesagem
        fields = ('id','url','peso','data','usuario')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    pesos = PesosSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email','password', 'pesos', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id','url', 'name')


class MensagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mensagem
        fields = ('id','url','conteudo')

