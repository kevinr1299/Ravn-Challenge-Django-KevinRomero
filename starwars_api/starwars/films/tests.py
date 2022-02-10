from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from starwars.films.models import Film
from starwars.films.serializer import FilmSerializer

fake = Faker()


class TestFilm(APITestCase):

    def setUp(self) -> None:
        self.film = Film.objects.create(
            name=fake.first_name(),
        )

    def test_print_film(self):
        self.assertEqual(
            str(self.film),
            self.film.name,
        )

    def test_film_serializer(self):
        serializer = FilmSerializer(self.film, context={
            'request': None,
        })
        self.assertEqual(
            serializer.data['url'],
            reverse('films:film', kwargs={
                'pk': self.film.id,
            }),
        )

    def test_fail_retrieve(self):
        response = self.client.get(
            reverse('films:film', kwargs={
                'pk': fake.pyint(min_value=100)
            })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve(self):
        response = self.client.get(
            reverse('films:film', kwargs={
                'pk': self.film.id,
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
