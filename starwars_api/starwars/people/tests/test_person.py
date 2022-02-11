from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from starwars.people.models.catalogues import (
    EyeColor,
    Gender,
    HairColor,
    SkinColor,
    Specie,
    World,
)
from starwars.people.models.person import Person
from starwars.people.serializers.person import PersonSerializer

fake = Faker()


def set_record_on_catalogues(test: APITestCase) -> None:
    test.eye_color = EyeColor.objects.create(
        name=fake.color_name(),
    )
    test.gender = Gender.objects.create(
        name=fake.pystr(max_chars=10),
    )
    test.hair_color = HairColor.objects.create(
        name=fake.color_name(),
    )
    test.skin_color = SkinColor.objects.create(
        name=fake.color_name(),
    )
    test.specie = Specie.objects.create(
        name=fake.pystr(max_chars=10),
    )
    test.world = World.objects.create(
        name=fake.pystr(max_chars=10),
    )


class TestPeopleModel(APITestCase):

    def setUp(self):
        set_record_on_catalogues(test=self)
        self.person = Person.objects.create(
            name=fake.first_name(),
            height=fake.pyfloat(min_value=0),
            mass=fake.pyfloat(min_value=0),
            birth_date=fake.date(),
            eye_color=self.eye_color,
            hair_color=self.hair_color,
            skin_color=self.skin_color,
            gender=self.gender,
            homeworld=self.world,
        )
        self.person.species.add(self.specie)

    def test_set_creation_date(self):
        self.assertIsNotNone(
            self.person.created_at,
        )
        self.assertIsNotNone(
            self.person.updated_at,
        )

    def test_serialize_person(self):
        serializer = PersonSerializer(self.person, context={
            'request': None,
        })
        self.assertEqual(
            serializer.data['url'],
            reverse('people:person', kwargs={
                'pk': self.person.id,
            }),
        )
        self.assertEqual(
            serializer.data['eye_color'],
            self.eye_color.name,
        )
        self.assertEqual(
            serializer.data['skin_color'],
            self.skin_color.name,
        )
        self.assertEqual(
            serializer.data['gender'],
            self.gender.name,
        )
        self.assertEqual(
            serializer.data['hair_color'],
            self.hair_color.name,
        )
        self.assertEqual(
            serializer.data['homeworld'],
            reverse('catalogues:world', kwargs={
                'pk': self.world.id
            })
        )
        self.assertIn(
            reverse('catalogues:specie', kwargs={
                'pk': self.specie.id,
            }),
            serializer.data['species'],
        )

    def test_retrieve_person(self):
        response = self.client.get(
            reverse('people:person', kwargs={
                'pk': self.person.id,
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fail_retrieve_person(self):
        response = self.client.get(
            reverse('people:person', kwargs={
                'pk': fake.pyint(min_value=100),
            }),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_people(self):
        response = self.client.get(
            reverse('people:people'),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertIn('next', response.data)
