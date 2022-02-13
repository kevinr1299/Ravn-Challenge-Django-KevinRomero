from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from faker import Faker

from starwars.people.admin import PersonAdmin
from starwars.people.forms import PersonForm
from starwars.people.models.person import Person
from starwars.people.tests.utils import PeopleTestUtils

fake = Faker()
User = get_user_model()


class TestPersonAdmin(TestCase):

    def setUp(self) -> None:
        self.site = AdminSite()

    def test_form_fild(self):
        personAdmin = PersonAdmin(Person, self.site)
        model_fields = [
            field.name
            for field in Person._meta.get_fields()
        ]
        form = personAdmin.get_form(None)
        for field in form._meta.fields:
            self.assertIn(field, model_fields)


class TestPersonForm(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username=fake.free_email(),
            email=fake.free_email(),
            password=fake.password(length=10),
        )
        PeopleTestUtils.set_people_record(test=self)

    def test_submit(self):
        data = {
            "name": fake.first_name(),
            "mass": fake.pyfloat(min_value=1),
            "height": fake.pyfloat(min_value=1),
            "birth_date": fake.date(end_datetime=timezone.now()),
            "hair_color": self.hair_color.id,
            "skin_color": self.skin_color.id,
            "eye_color": self.eye_color.id,
            "gender": self.gender.id,
            "specie": self.specie.id,
            "homeworld": self.world.id,
        }
        result = PersonForm(data).save()
        self.assertIsInstance(result, Person)
