import uuid

from django import forms
from django.utils.text import slugify
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Field, Fieldset, HTML
from crispy_forms.bootstrap import PrependedText
import autocomplete_light
from .models import Entry

class EntryForm(autocomplete_light.ModelForm):
    @property
    def helper(self):
        helper = FormHelper()
        helper.render_unmentioned_fields = True
        helper.form_tag = False

        helper.layout = Layout(
            Fieldset(
                _(u'People or organization'),
                Div(Div(Field('name', placeholder=_("People or organization name")), css_class="col-sm-6"),
                    Div(Field('category', placeholder=_("Category")), css_class="col-sm-6"),
                    css_class="row"
                ),
                Div(Div(Field('tags', placeholder=_("keyword, keyword 1, key word 2")), css_class="col-sm-12"),
                    css_class="row"
                ),
                Div(Div('description', css_class="col-sm-12"),
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
            Fieldset(
                _('Social web'),
                Div(Div(PrependedText('twitter', '@', placeholder=_("Twitter account")),
                        Field('facebook', placeholder=_("Facebook page")), css_class="col-sm-6"),
                    Div(Field('googleplus', placeholder=_("Google+ page")),
                        Field('linkedin', placeholder=_("LinkedIn page")), css_class="col-sm-6"),
                    css_class="row"
                ),
            ),
        )
        #Div('country', css_class="col-sm-6"),


        return helper

    class Meta:
        model = Entry
        exclude = ['slug']
        widgets = {
            'address': forms.Textarea(attrs={'cols':10, 'rows':3}),
            'description': forms.Textarea(attrs={'cols': 10, 'rows': 4}),
            'tags':autocomplete_light.widgets.TextWidget('TagAutocomplete'),
            'lat':forms.HiddenInput(),
            'lon':forms.HiddenInput(),
        }

    class Media:
        js = ["/static/thedirectory/js/map_mini.js"]

    def save(self, commit=True):
        u'''Add the slug value'''

        entry = super(EntryForm, self).save(commit=False)

        if not entry.slug:
            entry.slug = slugify(self.cleaned_data.get('name'))
            try:
                Entry.objects.get(slug=entry.slug)
                entry.slug = "%s-%s" % (entry.slug, str(uuid.uuid4())[:5])
            except Entry.DoesNotExist:
                pass
        if commit:
            entry.save()
            self.save_m2m()
        return entry
