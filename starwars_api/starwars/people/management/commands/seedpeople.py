import random

from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)
from django.db import (
    transaction,
    IntegrityError,
    ProgrammingError,
)
from faker import Faker

from starwars.people.models.catalogues import (
    EyeColor,
    Gender,
    HairColor,
    SkinColor,
    Specie,
    World,
)
from starwars.films.models import Film
from starwars.people.models.person import Person
from starwars.utils.models import CatalogueManager
from starwars.vehicles.models import Vehicle

fake = Faker()


class Command(BaseCommand):

    max_name = 'n'
    help = 'Create fake record to catalogues and people table'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            self.max_name,
            type=int,
            help='Number of people to insert',
        )

    def handle(self, *args, **options) -> None:
        max_record = options[self.max_name]

        with transaction.atomic():
            try:
                gender_list = [
                    Gender.objects.create(
                        name='Male',
                    ),
                    Gender.objects.create(
                        name='Female',
                    ),
                    Gender.objects.create(
                        name='Non binary',
                    ),
                ]
            except IntegrityError as e:
                raise CommandError(
                    'The genders have already been saving'
                ) from e
            except ProgrammingError as e:
                raise CommandError(
                    'Database issue: '
                    'execute the migrations',
                ) from e

            eye_list = CatalogueManager.seed_random(
                EyeColor,
                'eye color',
                max_record,
            )

            hair_list = CatalogueManager.seed_random(
                HairColor,
                'hair color',
                max_record,
            )

            skin_list = CatalogueManager.seed_random(
                SkinColor,
                'skin color',
                max_record,
            )

            specie_list = CatalogueManager.seed_random(
                Specie,
                'specie',
                max_record,
            )

            world_list = CatalogueManager.seed_random(
                World,
                'world',
                max_record,
            )

            vehicle_list = CatalogueManager.seed_random(
                Vehicle,
                'vehicle',
                max_record,
            )

            film_list = CatalogueManager.seed_random(
                Film,
                'film',
                max_record,
            )

            for _ in range(max_record):
                person = Person.objects.create(
                    name=fake.first_name(),
                    height=fake.pyfloat(min_value=0),
                    mass=fake.pyfloat(min_value=0),
                    birth_date=fake.date(),
                    eye_color=eye_list[random.randrange(
                        max_record,
                    )],
                    hair_color=hair_list[random.randrange(
                        max_record,
                    )],
                    skin_color=skin_list[random.randrange(
                        max_record,
                    )],
                    homeworld=world_list[random.randrange(
                        max_record,
                    )],
                    gender=gender_list[random.randrange(
                        len(gender_list),
                    )],
                )
                person.species.add(specie_list[random.randrange(
                    max_record,
                )])
                person.vehicles.add(vehicle_list[random.randrange(
                    max_record,
                )])

                film = film_list[random.randrange(
                    max_record,
                )]
                film.characters.add(person)

        self.stdout.write(self.style.SUCCESS(
            'The database has been filled in successfully',
        ))
