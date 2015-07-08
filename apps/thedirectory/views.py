import json
from django.shortcuts import render
from django.views.generic import DetailView

import django.http as http
import django.shortcuts as shortcuts
from django.http import HttpResponse

from .models import Category, Entry

class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['entry_list'] = Entry.objects.filter(category=self.object)

        return context



def json_map_entries_by_tags(request, tag):
    '''generates a json with list of pk for tag map filter

    simply pass the tag name to a template that generates the json data
    with a django-tagging templatetag'''

    entries = Entry.objects.filter(tags__name__in=[tag])
    data = []
    for entry in entries:
        data.append(entry.pk)
    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type='application/json')

def tags(request):
        return shortcuts.render_to_response("blog/tags.html")

def with_tag(request, tag):
    Entry.objects.filter(tags__name__in=[tag])

    return shortcuts.render_to_response(
        "thedirectory/map/map_entries_by_tags.js",
        dict(tag=tag, entries=entries)
    )