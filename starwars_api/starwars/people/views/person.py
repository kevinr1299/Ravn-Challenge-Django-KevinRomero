from rest_framework import generics

from starwars.people.models.person import Person
from starwars.people.serializers.person import PersonSerializer


class PeopleListView(generics.ListAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonView(generics.RetrieveAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
