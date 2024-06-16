from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import *


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height', )


class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Levels
        fields = ('winter', 'summer', 'autumn', 'spring', )


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.URLField()

    class Meta:
        model = Images
        fields = ('image', 'title', )



class PUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PUser
        fields = ('email',
                  'fam',
                  'name',
                  'otc',
                  'phone',
                  )


class PerevalSerializer(WritableNestedModelSerializer):  # drf writable nested
    user = PUserSerializer()
    coords = CoordsSerializer()
    level = LevelsSerializer()
    images = ImagesSerializer()

    class Meta:
        model = Pereval
        depth = 1
        fields = ('id',
                  'add_time',
                  'beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'user',
                  'coords',
                  'levels',
                  'status',
                  'images',
                  )
