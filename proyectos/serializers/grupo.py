from rest_framework import serializers
from proyectos.models import Perfil, Grupo

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'
