from django.test import TestCase

from .models import Music, Genre, Author, CustomUser
from .forms import MusicForm

# Create your tests here.
class MusicTestCase(TestCase):

    def setUp(self):
        pass

    def test_add_genre(self):
        Genre.objects.create(
            title='Suicidal Depressive Black Metal'
        )

    def test_add_author(self):
        Author.objects.create(
            title='Silencer',
            user='metallugabns@yandex.kx',
            followers='metallugabns@yandex.kx'
        )

    def test_add_music(self):
        Music.objects.create(
            status='BR',
            title='Sterile Nails and Thunderbowels',
            author='Silencer',
            duration="00:06",
            genre='Suicidal Depressive Black Metal',
        )
