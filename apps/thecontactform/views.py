from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from .forms import ContactForm

class ContactFormView(FormView):
    form_class = ContactForm

    template_name = 'thecontactform/contact_form.html'
    form_class = ContactForm
    success_url=reverse_lazy('success')

    def form_valid(self, form):
        form.send_email()
        return super(ContactFormView, self).form_valid(form)
