from datetime import datetime
from django.utils import timezone

from django.core.exceptions import ValidationError


class Validation:

    @staticmethod
    def validate_birth_date(value: datetime):
        if (value > timezone.now().date()):
            raise ValidationError(
                'The birth date might be less than today',
                params={'value': value},
            )

    @staticmethod
    def validate_min_value(value: float):
        if (value <= 0):
            raise ValidationError(
                'The value must be greater than zero',
                params={'value': value},
            )
