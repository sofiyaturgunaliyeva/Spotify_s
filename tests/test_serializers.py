#Vazifa. Spotify loyihasida quyidagi testlarni yozing:

# 1. Qo'shiqSerializerda fayl bo'yicha valid/invalid holatlar uchun 2 ta test qo'shing.
#
# 2. Qo'shiqSerializerda davomiylik bo'yicha valid/invalid holatlar uchun 2 ta test qo'shing.

from django.test import TestCase

from app1.models import *
from app1.serializers import *
# from rest_framework.authtoken.admin import User


class TestQoshiqSerializer(TestCase):
    def setUp(self):
        self.qoshiqchi = Qoshiqchi.objects.create(ism="John Doe", tugilgan_yil="1990", davlat="USA")
        self.albom = Albom.objects.create(nom="Best Hits", qoshiqchi=self.qoshiqchi)
        # self.mp3_file = SimpleUploadedFile("song.mp3", b"mp3_content", content_type="audio/mpeg")

    def test_valid_nom(self):
        data = {"nom": "Song.mp3","janr": "Pop","davomiylik": "00:03:30","albom": self.albom.id}
        serializer = QoshiqSerializer(data=data)
        assert serializer.is_valid() == True

    def test_invalid_nom(self):
        data = {"nom": "Song","janr": "Pop","davomiylik": "00:03:30","albom": self.albom.id}
        serializer = QoshiqSerializer(data=data)
        assert serializer.is_valid() == False

    def test_valid_davomiylik(self):
        data = {"nom": "Song.mp3","janr": "Pop","davomiylik": "00:03:30","albom": self.albom.id}
        serializer = QoshiqSerializer(data=data)
        assert serializer.is_valid() == True

    def test_invalid_davomiylik(self):
        data = {"nom": "Song","janr": "Pop","davomiylik": "00:08:30","albom": self.albom.id}
        serializer = QoshiqSerializer(data=data)
        assert serializer.is_valid() == False

