from django.urls import path

from starwars.people.views.person import (
    PeopleListView,
    PersonView,
)


urlpatterns = [
    path('', PeopleListView.as_view(), name='people'),
    path('<int:pk>/', PersonView.as_view(), name='person')
]
