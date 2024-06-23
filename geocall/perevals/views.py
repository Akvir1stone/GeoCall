from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, response, status
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

# Create your views here.


# class CoordsViewSet(viewsets.ModelViewSet):
#     queryset = Coords.objects.all()
#     serializer_class = CoordsSerializer
#
#
# class LevelsViewSet(viewsets.ModelViewSet):
#     queryset = Levels.objects.all()
#     serializer_class = LevelsSerializer
#
#
# class ImagesViewSet(viewsets.ModelViewSet):
#     queryset = Images.objects.all()
#     serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('user__email', )

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

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return response.Response({
                    'state': '1',
                    'message': 'Post changed'
                })
            else:
                return response.Response({
                    'state': '0',
                    'message': serializer.errors
                })
        else:
            return response.Response({
                'state': '0',
                'message': f'Error, {pereval.get_status_display()}'
            })

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        pass


# class PUserViewSet(viewsets.ModelViewSet):
#     queryset = PUser.objects.all()
#     serializer_class = PUserSerializer
