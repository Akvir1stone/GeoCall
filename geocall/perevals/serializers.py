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
    levels = LevelsSerializer()
    images = ImagesSerializer(many=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Pereval
        depth = 1
        fields = ('id',
                  'beauty_title',
                  'title',
                  'other_titles',
                  'connect',
                  'add_time',
                  'user',
                  'coords',
                  'levels',
                  'images',
                  'status',
                  )

    def create(self, validated_data):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('levels')
        images = validated_data.pop('images')

        user, created = PUser.objects.get_or_create(**user)
        coords = Coords.objects.create(**coords)
        level = Levels.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, levels=level, status='new')
        for image in images:
            data = image.pop('image')
            title = image.pop('title')
            Images.objects.create(image=data, title=title, per=pereval)

        return pereval

