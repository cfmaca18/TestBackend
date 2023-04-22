from rest_framework import serializers
from proyectos.models import Perfil, Ficha, Proyecto, Grupo, Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class GrupoSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(read_only=True)

    class Meta:
        model = Grupo
        fields = '__all__'
