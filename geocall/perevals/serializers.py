from rest_framework import serializers
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


class PerevalSerializer(serializers.ModelSerializer):  # drf writable nested
    class Meta:
        model = Pereval
        fields = ('add_time',
                  'beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'user',
                  'coords',
                  'levels',
                  'status',
                  )


class PUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PUser
        fields = ('email',
                  'fam',
                  'name',
                  'otc',
                  'phone',
                  )
