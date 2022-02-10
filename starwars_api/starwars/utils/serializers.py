from django.db.models import Model

from rest_framework import serializers


class NameRelatedField(serializers.SlugRelatedField):
    '''
        Create a slug serializer that returns a specific attribute of the model
    '''

    def __init__(self, slug_field: str = 'name', **kwargs):
        super().__init__(slug_field=slug_field, read_only=True, **kwargs)


def get_serializer_from_model(
    meta_model: Model,
    view_name: str,
) -> serializers.ModelSerializer:
    '''
        Return a model serializer with name and URL

        Parameters:
        meta_model(Model) A Django model
        view_name(str) Name of the endpoint
    '''

    class CatalogueSerializer(serializers.ModelSerializer):

        url = serializers.HyperlinkedIdentityField(
            view_name=view_name,
            read_only=True,
        )

        class Meta:
            model = meta_model
            fields = [
                'name',
                'url',
            ]

    return CatalogueSerializer
