from django.shortcuts import render
from django.views.generic import TemplateView
from apps.thedirectory.models import Entry
from apps.thecalendar.models import Event

class HomePageDetailView(TemplateView):
    template_name = 'thehomepage/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageDetailView,self).get_context_data(**kwargs)
        context['nb_entries'] = Entry.objects.count()
        context['nb_events'] = Event.objects.count()

        return context
