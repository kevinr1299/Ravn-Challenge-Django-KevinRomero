from unittest.mock import Mock

from django.db import models
from django.test import TestCase
from faker import Faker
from rest_framework import serializers

from starwars.utils.models import PrintShowsName
from starwars.utils.serializers import (
    NameRelatedField,
    get_serializer_from_model,
)

fake = Faker()


class FirstClass(PrintShowsName):
    pass


class SecondClass(PrintShowsName):

    def __init__(self, name: str) -> None:
        self.name = name


class TestUtils(TestCase):

    def test_fail_print(self):
        test_class = FirstClass()
        with self.assertRaises(AttributeError):
            str(test_class)

    def test_print(self):
        test_class = SecondClass(name=fake.first_name())
        self.assertEqual(
            str(test_class),
            test_class.name,
        )

    def test_serializer_generation(self):
        mock = Mock(spec=models.Model)
        serializer_class = get_serializer_from_model(mock, 'test')
        self.assertTrue(
            issubclass(
                serializer_class,
                serializers.ModelSerializer,
            )
        )

    def test_slug_override(self):
        field = NameRelatedField()
        self.assertIsInstance(
            field,
            serializers.SlugRelatedField,
        )
