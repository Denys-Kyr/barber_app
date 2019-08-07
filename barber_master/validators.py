from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_time(value):
    if not 0 < value < 180:
        raise ValidationError(_('Value should be in range from 0 to 180'), code='invalid')
    else:
        return value




