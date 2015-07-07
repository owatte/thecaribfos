#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import datetime
from django.db.models import Q
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse
#from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import render_to_response
from django.utils import timezone
from django.utils.translation import ugettext as _

from django.template import Context, RequestContext
#from django.shortcuts import render_to_response, get_object_or_404

from .models import Category, Event

class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['event_list'] = Event.objects.filter(category=self.object)
#~ #~
        return context


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

