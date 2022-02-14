from rest_framework import serializers

from starwars.people.models.person import Person
from starwars.utils.serializers import NameRelatedField


class PersonSerializer(serializers.ModelSerializer):

    hair_color = NameRelatedField()
    skin_color = NameRelatedField()
    eye_color = NameRelatedField()
    gender = NameRelatedField()
    homeworld = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='catalogues:world',
    )
    specie = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='catalogues:specie',
    )
    vehicles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='vehicles:vehicle',
    )
    films = serializers.HyperlinkedRelatedField(
        source='film_set',
        many=True,
        read_only=True,
        view_name='films:film',
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='people:person'
    )

    class Meta:
        model = Person
        fields = [
            'name',
            'height',
            'mass',
            'birth_date',
            'created_at',
            'updated_at',
            'hair_color',
            'skin_color',
            'eye_color',
            'gender',
            'homeworld',
            'specie',
            'vehicles',
            'films',
            'url',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
        ]
