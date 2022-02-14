from django.core.management.base import CommandError
from django.db import IntegrityError, ProgrammingError
from django.db.models import Model
from faker import Faker

fake = Faker()


class PrintShowsName:

    def __str__(self) -> str:
        return self.name


class CatalogueManager:

    @classmethod
    def seed_random(
        cls,
        model: Model,
        table_name: str,
        n_records: int,
    ) -> list:
        records = [
            model(
                name=fake.pystr(max_chars=10)
            )
            for _ in range(n_records)
        ]
        try:
            return model.objects.bulk_create(records)
        except IntegrityError as e:
            raise CommandError(
                'Bad luck, Faker repeated the value when creating '
                f'{table_name} records',
            ) from e
        except ProgrammingError as e:
            raise CommandError(
                'Database issue: '
                'execute the migrations',
            ) from e
