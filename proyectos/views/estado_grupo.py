from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from proyectos.models import Perfil, Ficha, Proyecto, Grupo, Estado
from proyectos.serializers.estado_grupo import PerfilSerializer, FichaSerializer, ProyectoSerializer, GrupoSerializer, EstadoSerializer

class GrupoList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


class GrupoDetail(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


class EstadoList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class EstadoDetail(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
