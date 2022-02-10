from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from starwars.vehicles.models import Vehicle
from starwars.vehicles.serializer import VehicleSerializer

fake = Faker()


class TestFilm(APITestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle.objects.create(
            name=fake.first_name(),
        )

    def test_print_film(self):
        self.assertEqual(
            str(self.vehicle),
            self.vehicle.name,
        )

    def test_film_serializer(self):
        serializer = VehicleSerializer(self.vehicle, context={
            'request': None,
        })
        self.assertEqual(
            serializer.data['url'],
            reverse('vehicles:vehicle', kwargs={
                'pk': self.vehicle.id,
            }),
        )

    def test_fail_retrieve(self):
        response = self.client.get(
            reverse('vehicles:vehicle', kwargs={
                'pk': fake.pyint(min_value=100)
            })
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve(self):
        response = self.client.get(
            reverse('vehicles:vehicle', kwargs={
                'pk': self.vehicle.id,
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
