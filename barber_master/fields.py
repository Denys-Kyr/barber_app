from django.db.models.fields import PositiveIntegerRelDbTypeMixin, IntegerField
from django.utils.translation import ugettext_lazy as _


class TimeForCuttingField(PositiveIntegerRelDbTypeMixin, IntegerField):
    description = _("Positive small integer from 0 to 180")

    def get_internal_type(self):
        return "PositiveSmallIntegerField"

    def formfield(self, **kwargs):
        return super().formfield(**{
            'min_value': 0,
            'max_value': 180,
            **kwargs,
        })
