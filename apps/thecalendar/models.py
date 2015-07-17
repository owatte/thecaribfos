from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

from taggit.managers import TaggableManager

from apps.thecarib.models import Country

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(_("Name"),
                             max_length=25)
    slug = models.SlugField(_("Slug"),
                            max_length=25)
    description = models.TextField(_("Description"),
                                   max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

@python_2_unicode_compatible
class Event(models.Model):

    DRAFT = 'draft'
    PENDING = 'pending'
    PUBLISHED = 'published'
    PUB_STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (PENDING, _('pending')),
        (PUBLISHED, _('published')),
    )

    TENTATIVE = 'tentative'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = (
        (TENTATIVE, _("tentative")),
        (CONFIRMED, _("confirmed")),
        (CANCELLED, _("cancelled")),
    )

    country = models.ForeignKey(Country)
    category = models.ForeignKey(Category)
    tags = TaggableManager(verbose_name = _("Tag(s)"),
                           blank=True)
    status = models.CharField(_("Status"),
                              max_length=10,
                              choices=STATUS_CHOICES,
                              default=PENDING)
    dtstart = models.DateTimeField(_("From"))
    dtend = models.DateTimeField(_("To"))
    allday = models.BooleanField(_("All day"))
    summary = models.CharField(_("Title"),
                               max_length=75)
    description = models.TextField(_("Description"),
                                   help_text=_("Use Markdown to format you description text"))
    email = models.EmailField(_("Email"),
                              help_text=_("Email are not published on the website."))
    web = models.URLField(_("Web"),
                               max_length=250)
    #~ location = models.CharField(_("Location"),
                                    #~ max_length=250)
    lat = models.FloatField(_("Latitude"), null=True)
    lon = models.FloatField(_("Longitude"), null=True)
    address = models.TextField(_("Address"),
                               max_length=250)

    slug = models.SlugField(_("Slug"),
                            max_length=100)
    sequence = models.SmallIntegerField(_("Update number"), default=0)
    creation_date = models.DateTimeField(_("Created on"),
                                         auto_now_add=True)
    creation_date = models.DateTimeField(_("Last modification"),
                                         auto_now=True)
    pub_status = models.CharField(_("Publication status"),
                                  max_length=10,
                                  choices=PUB_STATUS_CHOICES,
                                  default=PENDING)

    def __str__(self):
        return self.summary

    def save(self, *args, **kwargs):
        ''' increases the sequence number
        '''
        self.sequence += 1
        super(Event, self).save(*args, **kwargs)

    class Meta:
        ordering = ["dtstart", "country", "summary" ]

