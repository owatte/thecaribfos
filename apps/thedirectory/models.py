from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
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
    creation_user = models.ForeignKey(User)
    description = models.TextField(_("Description"),
                                   help_text=_("Use Markdown to format you description text"))
    address = models.TextField(_("Address"), null=True, blank=True)
    email = models.EmailField(_("Email"),
                              help_text=_("Email are not published on the website."))
    web = models.URLField(_("Web"),
                               max_length=250)
    lat = models.FloatField(_("Latitude"), null=True)
    lon = models.FloatField(_("Longitude"), null=True)
    sequence = models.SmallIntegerField(_("Update number"), default=0)
    creation_date = models.DateTimeField(_("Created on"),
                                         auto_now_add=True)
    lastupdate_date = models.DateTimeField(_("Last modification"),
                                         auto_now=True)

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

    def save(self, *args, **kwargs):
        ''' increases the sequence number
        '''
        self.sequence += 1
        super(Entry, self).save(*args, **kwargs)

    class Meta:
        ordering = ["name", "country"]
        verbose_name_plural = "Entries"
