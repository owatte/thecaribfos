from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Field, Fieldset, HTML
from crispy_forms.bootstrap import PrependedText

class ContactForm(forms.Form):

    name = forms.CharField(label=_('Your name'),
                           max_length=80,
                           required=True
    )
    email = forms.EmailField(label=_('Your email'),
                             max_length=80,
                             required=True
    )
    subject = forms.CharField(label=_('Your message subject'),
                              max_length=80,
                              required=True
    )
    message = forms.CharField(label=_('Your message'),
                              max_length=80,
                              widget=forms.Textarea,
                              required=True
    )

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False

        helper.layout = Layout(
            Fieldset(
                _(u'You'),
                Div(Div(Field('name'), css_class="col-md-12"),
                    css_class="row"
                ),
                Div(Div(Field('email'), css_class="col-md-12"),
                    css_class="row"
                ),
            ),
            Fieldset(
                _(u'Your message'),



                Div(Div(PrependedText('subject', '[The Carib FOS]'), css_class="col-md-12"),
                    css_class="row"
                ),
                Div(Div(Field('message'), css_class="col-md-12"),
                css_class="row"
                ),
            ),
        )
        return helper

    def send_email(self):
        send_mail(
            "{} {}".format(settings.EMAIL_PREFIX, self.cleaned_data['subject']),
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            settings.MANAGERS,
            fail_silently=False
        )
        return True


