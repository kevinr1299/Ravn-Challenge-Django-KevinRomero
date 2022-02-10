from django.urls import path

from starwars.people.views.catalogues import (
    EyeColorRetrieveView,
    GenderRetrieveView,
    HairColorRetrieveView,
    SkinColorRetrieveView,
    SpecieRetrieveView,
    WorldRetrieveView,
)


urlpatterns = [
    path(
        'eye-colors/<int:pk>/',
        EyeColorRetrieveView.as_view(),
        name='eye_color',
    ),
    path(
        'genders/<int:pk>/',
        GenderRetrieveView.as_view(),
        name='gender',
    ),
    path(
        'hair-colors/<int:pk>/',
        HairColorRetrieveView.as_view(),
        name='hair_color',
    ),
    path(
        'skin-colors/<int:pk>/',
        SkinColorRetrieveView.as_view(),
        name='skin_color',
    ),
    path(
        'species/<int:pk>/',
        SpecieRetrieveView.as_view(),
        name='specie',
    ),
    path(
        'worlds/<int:pk>/',
        WorldRetrieveView.as_view(),
        name='world'
    ),
]
