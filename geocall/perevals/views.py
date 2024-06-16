from django.shortcuts import render
from rest_framework import viewsets, response, status


from .serializers import *

# Create your views here.


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Levels.objects.all()
    serializer_class = LevelsSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data['id'],
            })
        print(serializer.errors)
        if status.HTTP_400_BAD_REQUEST:
            return response.Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad request',
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return response.Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Data base error',
                'id': None,
            })


class PUserViewSet(viewsets.ModelViewSet):
    queryset = PUser.objects.all()
    serializer_class = PUserSerializer
