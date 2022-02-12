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
        'specie',
        'homeworld',
        'vehicles',
    )


class GenderAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Person, PersonAdmin)
admin.site.register(HairColor)
admin.site.register(SkinColor)
admin.site.register(EyeColor)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Specie)
admin.site.register(World)
