from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager
from apps.thecarib.models import Country

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(_("Name"),
                             max_length=75)
    slug = models.SlugField(_("Slug"),
                            max_length=25)
    description = models.TextField(_("Description"),
                                   max_length=250,
                                   blank=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

@python_2_unicode_compatible
class Entry(models.Model):
    name = models.CharField(_("Name"),
                             max_length=75)
    slug = models.SlugField(_("Slug"),
                            max_length=100)
    country = models.ForeignKey(Country)
    category = models.ForeignKey(Category)
    tags = TaggableManager(verbose_name = _("Tag(s)"),
                           blank=True)
    description = models.TextField(_("Description"),
                                   help_text=_("Use Markdown to format you description text"))
    address = models.TextField(_("Address"), null=True, blank=True)
    email = models.EmailField(_("Email"),
                              help_text=_("Email are not published on the website."))
    web = models.URLField(_("Web"),
                               max_length=250)
    lat = models.FloatField(_("Latitude"), null=True)
    lon = models.FloatField(_("Longitude"), null=True)
    twitter =  models.CharField(_("Twitter account"),
                             max_length=75,
                             null=True,
                             blank=True)
    facebook = models.CharField(_("Facebook page"),
                             max_length=75,
                             null=True,
                             blank=True)
    googleplus = models.CharField(_("Google plus page"),
                             max_length=75,
                             null=True,
                             blank=True)
    linkedin = models.CharField(_("LinkedIn page"),
                             max_length=75,
                             null=True,
                             blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name", "country"]
        verbose_name_plural = "Entries"
