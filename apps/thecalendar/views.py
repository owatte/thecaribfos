#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import datetime
from django.db.models import Q
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView
from django.shortcuts import render_to_response
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse_lazy

from django.template import Context, RequestContext
from .models import Category, Event
from .forms import EventForm

class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.filter(category=self.object)

        return context

class EventCreateView(CreateView):
    form_class=EventForm
    template_name='thecalendar/page_form_event_add.html'
    success_url=reverse_lazy('success')

    def get_form_kwargs(self):
        kwargs = super(EventCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs.copy()

class EventUpdateView(UpdateView):
    form_class=EventForm
    model = Event
    slug_field = 'slug'
    template_name='thecalendar/page_form_event_add.html'
    success_url=reverse_lazy('success')
    context_object_name='event'

    def get_form_kwargs(self):
        kwargs = super(EventUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs.copy()


def fullcalendar_events_json(request):
    '''generates events json file needed for fullcalendar
    see http://fullcalendar.io/
    '''

    start = datetime.datetime.strptime(request.GET.get('start', '1970-01-01'), '%Y-%m-%d')
    end = datetime.datetime.strptime(request.GET.get('end', '1970-01-01'), '%Y-%m-%d')

    #events = Event.objects.filter(Q(dtstart__gte=start, dtend__lte=end)|Q(dtstart__lte=start, dtend__gte=end))
    events = Event.objects.all()

    country = request.GET.get('country', False)
    if country:
        events = events.filter(country__iso=country)
    data = []

    for event in events:
        data.append({
        'id': event.id,
        'title': event.summary,
        'start': event.dtstart.strftime('%Y-%m-%d'),
        'end': event.dtend.strftime('%Y-%m-%d'),
        'url': reverse('thecalendar:event_detail', args=[event.slug])
        })
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

