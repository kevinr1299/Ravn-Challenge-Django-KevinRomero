from django.urls import path

from starwars.films.views import FilmRetrieveView

urlpatterns = [
    path('<int:pk>/', FilmRetrieveView.as_view(), name='film'),
]
