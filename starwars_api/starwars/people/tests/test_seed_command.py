from io import StringIO
from unittest.mock import patch

from django.core.management import call_command
from django.db.models import Model
from django.test import TestCase
from faker import Faker

from starwars.people.models.person import Person

fake = Faker()


def bulk_create_effect(model: Model, table_name: str, n_records: int):
    return [
        model.objects.create(
            name=fake.pystr(max_chars=10)
        )
        for _ in range(n_records)
    ]


def bulk_define_list(records: list):
    print(records)
    for model in records:
        print(model)
        model.save()


class TestSeedCommand(TestCase):

    def test_command_execution(self):
        out = StringIO()
        with patch(
            'starwars.utils.models.CatalogueManager.seed_random',
            side_effect=bulk_create_effect,
        ):
            with patch(
                'starwars.people.management.commands'
                '.seedpeople.Command._create_genders',
                side_effect=bulk_define_list,
            ):
                call_command('seedpeople', 20, stdout=out)
        self.assertIn(
            'The database has been filled in successfully',
            out.getvalue(),
        )
        self.assertTrue(
            Person.objects.all(),
        )
