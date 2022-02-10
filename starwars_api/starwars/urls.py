"""starwars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/people/', include(
        ('starwars.people.urls.person', 'people'),
        namespace='people',
    )),
    path('api/', include(
        ('starwars.people.urls.catalogues', 'catalogues'),
        namespace='catalogues',
    )),
    path('api/films/', include(
        ('starwars.films.urls', 'films'),
        namespace='films',
    )),
    path('api/vehicles/', include(
        ('starwars.vehicles.urls', 'vehicles'),
        namespace='vehicles',
    )),
]
