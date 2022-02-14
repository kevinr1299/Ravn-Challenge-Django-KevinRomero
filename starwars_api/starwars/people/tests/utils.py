from unittest import TestCase

from faker import Faker

from starwars.people.models.catalogues import (
    EyeColor,
    Gender,
    HairColor,
    SkinColor,
    Specie,
    World,
)
from starwars.people.models.person import Person

fake = Faker()


class PeopleTestUtils:

    @staticmethod
    def set_people_record(test: TestCase) -> None:
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
        test.person = Person.objects.create(
            name=fake.first_name(),
            height=fake.pyfloat(min_value=0),
            mass=fake.pyfloat(min_value=0),
            birth_date=fake.date(),
            eye_color=test.eye_color,
            hair_color=test.hair_color,
            skin_color=test.skin_color,
            gender=test.gender,
            specie=test.specie,
            homeworld=test.world,
        )
