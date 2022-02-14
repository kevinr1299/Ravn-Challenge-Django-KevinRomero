from datetime import timedelta
from unittest.mock import patch

from django.core.exceptions import ValidationError
from django.db import models
from django.test import TestCase
from django.utils import timezone
from faker import Faker
from rest_framework import serializers

from starwars.utils.models import (
    PrintShowsName,
    CatalogueManager,
)
from starwars.utils.serializers import (
    NameRelatedField,
    get_serializer_from_model,
)
from starwars.utils.validators import Validation

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
        with patch('django.db.models.Model'):
            serializer_class = get_serializer_from_model(models.Model, 'test')
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


class TestCatalogueManager(TestCase):

    def test_seed_random(self):
        with patch('django.db.models.Model'):
            result = CatalogueManager.seed_random(models.Model, 'model', 10)
            self.assertIsNotNone(result)


class TestValidator(TestCase):

    def test_wrong_birth_date(self):
        with self.assertRaises(ValidationError):
            birth_date = (
                timezone.now()
                + timedelta(days=fake.pyint(min_value=1))
            )
            Validation.validate_birth_date(birth_date.date())

    def test_correct_birth_date(self):
        Validation.validate_birth_date(timezone.now().date())
        self.assertTrue(True)

    def test_lower_value(self):
        with self.assertRaises(ValidationError):
            Validation.validate_min_value(
                fake.pyfloat(max_value=0),
            )

    def test_greater_value(self):
        Validation.validate_min_value(
            fake.pyfloat(min_value=1),
        )
        self.assertTrue(True)
