from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy

from .views import ContactFormView

urlpatterns = [
    # entry details
    url(r'^$',
        ContactFormView.as_view(),
        name = 'contact-form'
    ),
]


