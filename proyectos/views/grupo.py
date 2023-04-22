from rest_framework import viewsets

from proyectos.serializers.grupo import *

class GrupoList(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class GrupoDetail(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
