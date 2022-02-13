from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from starwars.people.serializers.person import PersonSerializer
from starwars.people.tests.utils import PeopleTestUtils

fake = Faker()


class TestPeopleModel(APITestCase):

    def setUp(self):
        PeopleTestUtils.set_people_record(test=self)

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
        self.assertEqual(
            reverse('catalogues:specie', kwargs={
                'pk': self.specie.id,
            }),
            serializer.data['specie'],
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
