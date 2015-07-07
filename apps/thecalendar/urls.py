from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import EventForm
from .models import Category, Event
from .views import fullcalendar_events_json
from .views import CategoryDetailView

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


    #~ #url(r'^(?P<year>d{4})/$', YearArchiveView.as_view(template_name='events/index.html', model=Event)),
    # index (fullcalendar)
    #~ url(r'^$',
        #~ ListView.as_view(model = Event,
                         #~ template_name = 'thecalendar/fullcalendar.html'
        #~ ),
        #~ name="fullcalendar"
    #~ ),

    # form add entry
    url(r'^event/add/$',
        login_required(
            CreateView.as_view(
                form_class=EventForm,
                template_name='thecalendar/page_form_event_add.html',
                success_url=reverse_lazy('success'))
            ),
            name="form_event_add",
    ),

    # event details
    url(r'^(?P<slug>[-\w]+)/$',
        DetailView.as_view(model = Event,
                           template_name ='thecalendar/details.html'
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
