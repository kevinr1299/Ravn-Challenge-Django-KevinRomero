from django import forms

from starwars.people.models.person import Person
from starwars.utils.validators import Validation


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        exclude = [
            'ctreated_at',
            'updated_at',
        ]

    def clean_birth_date(self):
        value = self.cleaned_data['birth_date']
        Validation.validate_birth_date(value)
        return value

    def clean_mass(self):
        value = self.cleaned_data['mass']
        Validation.validate_min_value(value)
        return value

    def clean_height(self):
        value = self.cleaned_data['height']
        Validation.validate_min_value(value)
        return value
