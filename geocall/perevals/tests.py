from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .serializers import *

# Create your tests here.


class PerevalAPITests(APITestCase):
    def setUp(self):
        self.user1 = PUser.objects.create(email='ddd@ddd.ddd', fam='ddd', name='ddd', otc='ddd', phone='143324')
        self.user2 = PUser.objects.create(email='aaa@ddd.ddd', fam='aaa', name='aaa', otc='aaa', phone='476456')
        self.coords1 = Coords.objects.create(latitude=12, longitude=21, height=32)
        self.coords2 = Coords.objects.create(latitude=65, longitude=56, height=76)
        self.levels1 = Levels.objects.create(winter='lvl1', summer='lvl1', autumn='lvl1', spring='lvl1')
        self.levels2 = Levels.objects.create(winter='lvl2', summer='lvl2', autumn='lvl2', spring='lvl2')
        self.image = Images.objects.create(image='https://hips.hearstapps.com/hmg-prod/images/ama-dablam-mountain-peak-view-from-chola-pass-royalty-free-image-1623254695.jpg',
                                           title='asdad')
        self.pereval1 = Pereval.objects.create(beauty_title='aaa',
                                               title='aaa',
                                               user=self.user1,
                                               coords=self.coords1,
                                               levels=self.levels1,
                                               status='new')
        self.pereval2 = Pereval.objects.create(beauty_title='bbb',
                                               title='bbb',
                                               user=self.user2,
                                               coords=self.coords2,
                                               levels=self.levels2,
                                               status='new')
        self.pereval_pending = Pereval.objects.create(beauty_title='aaa',
                                                      title='aaa',
                                                      user=self.user1,
                                                      coords=self.coords1,
                                                      levels=self.levels1,
                                                      status='pending')

    def test_get_list(self):
        url = reverse('pereval-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval1, self.pereval2, self.pereval_pending], many=True).data
        self.assertEquals(response.data, serializer_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 3)

    def test_get_list_email_arg(self):
        # url = reverse('pereval-list')
        response = self.client.get('/Pereval/?user__email=ddd@ddd.ddd')
        serializer_data = PerevalSerializer([self.pereval1, self.pereval_pending], many=True).data
        self.assertEquals(response.data, serializer_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)

    def test_get_detail(self):
        url = reverse('pereval-detail', args=(self.pereval1.id, ))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval1).data
        self.assertEquals(response.data, serializer_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class SerializersTests(TestCase):
    def setUp(self):
        self.user1 = PUser.objects.create(email='ddd@ddd.ddd', fam='ddd', name='ddd', otc='ddd', phone='143324')
        self.user2 = PUser.objects.create(email='aaa@ddd.ddd', fam='aaa', name='aaa', otc='aaa', phone='476456')
        self.coords1 = Coords.objects.create(latitude=12, longitude=21, height=32)
        self.coords2 = Coords.objects.create(latitude=65, longitude=56, height=76)
        self.levels1 = Levels.objects.create(winter='lvl1', summer='lvl1', autumn='lvl1', spring='lvl1')
        self.levels2 = Levels.objects.create(winter='lvl2', summer='lvl2', autumn='lvl2', spring='lvl2')
        self.image = Images.objects.create(image='https://hips.hearstapps.com/hmg-prod/images/ama-dablam-mountain-peak-view-from-chola-pass-royalty-free-image-1623254695.jpg',
                                           title='asdad')
        self.pereval1 = Pereval.objects.create(beauty_title='aaa',
                                               title='aaa',
                                               user=self.user1,
                                               coords=self.coords1,
                                               levels=self.levels1,
                                               status='new')
        self.pereval2 = Pereval.objects.create(beauty_title='bbb',
                                               title='bbb',
                                               user=self.user2,
                                               coords=self.coords2,
                                               levels=self.levels2,
                                               status='new')
        self.pereval_pending = Pereval.objects.create(beauty_title='aaa',
                                                      title='aaa',
                                                      user=self.user1,
                                                      coords=self.coords1,
                                                      levels=self.levels1,
                                                      status='pending')

    def test_coords_serializer(self):
        serializer_data = CoordsSerializer([self.coords1, self.coords2], many=True).data
        expected_data = [
            {'latitude': 12.0, 'longitude': 21.0, 'height': 32.0, 'id': self.coords1.id},
            {'latitude': 65.0, 'longitude': 56.0, 'height': 76.0, 'id': self.coords2.id}
        ]
        self.assertEquals(serializer_data, expected_data)

    def test_coords_levels(self):
        serializer_data = LevelsSerializer([self.levels1, self.levels2], many=True).data
        expected_data = [
            {'winter': 'lvl1', 'summer': 'lvl1', 'autumn': 'lvl1', 'spring': 'lvl1', 'id': self.levels1.id},
            {'winter': 'lvl2', 'summer': 'lvl2', 'autumn': 'lvl2', 'spring': 'lvl2', 'id': self.levels2.id}
        ]
        self.assertEquals(serializer_data, expected_data)

    def test_coords_images(self):
        serializer_data = ImagesSerializer(self.image).data
        expected_data = {
            'image': 'https://hips.hearstapps.com/hmg-prod/images/ama-dablam-mountain-peak-view-from-chola-pass-royalty-free-image-1623254695.jpg',
            'title': 'asdad',
            'id': self.image.id
        }
        self.assertEquals(serializer_data, expected_data)

    def test_coords_users(self):
        serializer_data = PUserSerializer([self.user1, self.user2], many=True).data
        expected_data = [
            {'email': 'ddd@ddd.ddd', 'fam': 'ddd', 'name': 'ddd', 'otc': 'ddd', 'phone': '143324', 'id': self.user1.id},
            {'email': 'aaa@ddd.ddd', 'fam': 'aaa', 'name': 'aaa', 'otc': 'aaa', 'phone': '476456', 'id': self.user2.id}
        ]
        self.assertEquals(serializer_data, expected_data)

    def test_coords_perevals(self):
        serializer_data = PerevalSerializer([self.pereval1, self.pereval2, self.pereval_pending], many=True).data
        expected_data = [
            {
                'id': 16,
                'beauty_title': 'aaa',
                'title': 'aaa',
                'other_titles': None,
                'connect': None,
                'add_time': PerevalSerializer(self.pereval1).data['add_time'],
                'user': PUserSerializer(self.user1).data,
                'coords': CoordsSerializer(self.coords1).data,
                'levels': LevelsSerializer(self.levels1).data,
                'images': [],
                'status': 'new'
            },
            {
                'id': 17,
                'beauty_title': 'bbb',
                'title': 'bbb',
                'other_titles': None,
                'connect': None,
                'add_time': PerevalSerializer(self.pereval2).data['add_time'],
                'user': PUserSerializer(self.user2).data,
                'coords': CoordsSerializer(self.coords2).data,
                'levels': LevelsSerializer(self.levels2).data,
                'images': [],
                'status': 'new'
            },
            {
                'id': 18,
                'beauty_title': 'aaa',
                'title': 'aaa',
                'other_titles': None,
                'connect': None,
                'add_time': PerevalSerializer(self.pereval_pending).data['add_time'],
                'user': PUserSerializer(self.user1).data,
                'coords': CoordsSerializer(self.coords1).data,
                'levels': LevelsSerializer(self.levels1).data,
                'images': [],
                'status': 'pending'
            }
        ]
        self.assertEquals(serializer_data, expected_data)

