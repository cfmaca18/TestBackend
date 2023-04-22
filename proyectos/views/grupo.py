from rest_framework import viewsets
from proyectos.models import Grupo
from proyectos.serializers.grupo import GrupoSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

    # Definir el diccionario de acciones para permitir 'list' y 'retrieve'
    # (métodos HTTP 'GET') en el ViewSet.
    # También puedes agregar otros métodos como 'create', 'update', 'partial_update',
    # 'destroy' y 'custom_action'.
    action = {
        'list': 'get',
        'retrieve': 'get',
    }
