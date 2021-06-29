from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import tecnologia_service
from ..serializers import tecnologia_serializer
from ..entidades import tecnologia


class TecnologiaList(APIView):
    permission_classes = [IsAuthenticated]  # Apenas se o usuário estiver autenticado
    def get(self, request, format=None):
        tecnologias = tecnologia_service.listar_tecnologias()
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = tecnologia_serializer.TecnologiaSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_service.cadastrar_tecnologia(tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TecnologiaDetail(APIView):
    def get(self, request, id, format=None):
        tecnologia = tecnologia_service.get_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        tecnologia_antiga = tecnologia_service.get_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia_antiga, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_service.editar_tecnologia(tecnologia_antiga, tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        tecnologia = tecnologia_service.get_tecnologia_id(id)
        tecnologia_service.remover_tecnologia(tecnologia)
        return Response(status=status.HTTP_204_NO_CONTENT)

