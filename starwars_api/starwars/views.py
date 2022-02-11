from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="StarWars API",
      default_version='v1',
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   public=True,
)
