import uuid

from django import forms
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, HTML, Layout, Fieldset
from crispy_forms.bootstrap import PrependedText
from django.template import RequestContext

from .models import Event


class EventForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EventForm, self).__init__(*args, **kwargs)
        #user = kwargs.pop('user', None)

    @property
    def helper(self):
        helper = FormHelper()
        helper.render_unmentioned_fields = True
        helper.form_tag = False

        helper.layout = Layout(
            Fieldset(
                _(u'Event'),
                Div(Div(Field('summary', placeholder=_(u'Event summary')), css_class='col-sm-6'),
                    Div(Field('category', placeholder=_("Category")), css_class='col-sm-6'),
                    css_class='row'
                ),

                Div(Div(Field('tags', placeholder=_("keyword, keyword 1, key word 2")), css_class="col-sm-12"),
                    css_class="row"
                ),
                Div(Div(Field('description', help_text=_('tada')), css_class="col-sm-12"),
                    css_class="row"
                ),
            ),
            Fieldset(
                _(u'Contact'),
                Div(Div(Field('email', placeholder=_("Contact Email")), css_class="col-sm-6"),
                    Div(Field('web', placeholder=_("Web site URL")), css_class="col-sm-6"),
                    css_class="row"
                ),
            ),
            Fieldset(
                _(u'Date'),
                Div(Div(Field('dtstart', placeholder=_(u'From')), css_class='col-sm-6'),
                    Div(Field('dtend', placeholder=_(u'To')), css_class='col-sm-6'),
                    css_class='row'
                ),
                Div(Div(Field('allday'), css_class='col-sm-12'),
                    css_class='row'
                ),
            ),
            Fieldset(
                _(u'Location'),
                Div(Div(Field('country', placeholder=_("country")), HTML('''{% load i18n %}<p class="help-block"><button id="geosearch-button" type="button" class="btn btn-default">
                {% trans 'Geolocate' %}</button> Try to geolocate from the given address.
                </p>'''), css_class="col-sm-6"),
                    Div(Field('address', placeholder=_(
'''Street


\n


 ZipCode City''')), css_class="col-sm-6"),
                    css_class="row"
                ),
                Div(Div(HTML('''<div style="height:350px;" id="map"></div><br>'''), css_class="col-sm-12"),
                    css_class="row"),
                Div(Div(Field('lat', placeholder=_("Location latitude")), css_class="col-sm-6"),
                    Div(Field('lon', placeholder=_("Location longitude")), css_class="col-sm-6"),
                    css_class="row"),
            ),
        )

        return helper

    class Meta:
        model = Event
        widgets = {
            #'description' : MarkdownInput(attrs={'cols': 10, 'rows': 4}),
            'description': forms.Textarea(attrs={'cols': 10, 'rows': 6}),
            'address': forms.Textarea(attrs={'cols': 10, 'rows': 3}),
            'dtstart': forms.DateInput(attrs={'class': 'datepicker'}),
            'dtend': forms.DateInput(attrs={'class': 'datepicker'}),
            'lat':forms.HiddenInput(),
            'lon':forms.HiddenInput(),
       }
        #fields = "__all__"
        exclude =['slug', 'pub_status', 'status', 'sequence']

    class Media:
        js = ["/static/thedirectory/js/map_mini.js"]

    def save(self, commit=True):
        u'''Add the slug value'''

        event = super(EventForm, self).save(commit=False)

        if not event.slug:
            event.slug = slugify(self.cleaned_data.get('summary'))
            try:
                Event.objects.get(slug=event.slug)
                event.slug = "%s-%s" % (event.slug, str(uuid.uuid4())[:5])
            except Event.DoesNotExist:
                pass
        if commit:
            event.creation_user = self.user
            event.save()
            self.save_m2m()
        return event
