from django.contrib import admin

from starwars.people.models.catalogues import (
    EyeColor,
    Gender,
    HairColor,
    SkinColor,
    Specie,
    World,
)
from starwars.people.models.person import Person


class PersonAdmin(admin.ModelAdmin):

    fields = (
        'name',
        'height',
        'mass',
        'birth_date',
        'hair_color',
        'skin_color',
        'eye_color',
        'gender',
        'species',
        'homeworld',
        'vehicles',
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(HairColor)
admin.site.register(SkinColor)
admin.site.register(EyeColor)
admin.site.register(Gender)
admin.site.register(Specie)
admin.site.register(World)
