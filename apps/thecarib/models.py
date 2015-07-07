from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(_("Name"),
                            max_length=75)

    iso = models.SlugField(_("Iso code"),
                            max_length="5",
                            help_text=_("iso 3166 code"),
                            unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Countries"
