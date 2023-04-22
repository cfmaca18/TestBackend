from rest_framework import serializers
from proyectos.models import Perfil, Ficha, Proyecto, Grupo, Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

    def validate_estado(self, value):
        try:
            estado = Estado.objects.get(id=value)
        except Estado.DoesNotExist:
            raise serializers.ValidationError("Estado no existe")
        return estado.id

        


class GrupoSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer()

    class Meta:
        model = Grupo
        fields = '__all__'
