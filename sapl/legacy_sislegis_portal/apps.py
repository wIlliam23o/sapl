from django import apps
from django.utils.translation import ugettext_lazy as _


class AppConfig(apps.AppConfig):
    name = 'sapl.legacy_sislegis_portal'
    label = 'legacy_sislegis_portal'
    verbose_name = _('Import Sislegis Portal')
