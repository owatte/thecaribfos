from django.views.generic import DetailView

from .models import Country
from apps.thedirectory.models import Entry
from apps.thecalendar.models import Event


class CountryDetail(DetailView):

    model = Country
    context_object_name = 'country'
    slug_field = 'iso'

    def get_context_data(self, **kwargs):
        context = super(CountryDetail, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.filter(country=self.object)
        context['entry_list'] = Entry.objects.filter(country=self.object)
        context['country_list'] = Country.objects.all().order_by('?')[:3]

        return context
