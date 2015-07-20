from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import EventForm
from .models import Category, Event
from .views import fullcalendar_events_json, CategoryDetailView, EventCreateView

urlpatterns = [
    #index
    url(r'^agenda/$',
    TemplateView.as_view(
            template_name = 'thecalendar/page_agenda.html'
        ),
        name = 'agenda'
    ),

    # json for zabuto calendar
    url(r'^json$',
        fullcalendar_events_json,
        name = 'fullcalendar_json'
    ),

    # form add event
    url(r'^event/add/$',
            login_required(EventCreateView.as_view()
        ),
        name="form_event_add",
    ),

    # event details
    url(r'^(?P<slug>[-\w]+)/$',
        DetailView.as_view(model = Event,
                           context_object_name='event',
                           template_name ='thecalendar/event_detail.html'
        ),
        name = 'event_detail'
    ),
    # Category details
    url(r'^categories/(?P<slug>[-\w\d]+)/$',
        CategoryDetailView.as_view(),
        name = 'category_detail'
    ),

    # Categories list
    url(r'^categories/$',
        ListView.as_view(
            model = Category,
            context_object_name = 'categories',
        ),
        name = "category_list"
    ),
]
