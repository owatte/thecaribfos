from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, ListView, TemplateView

from .forms import EntryForm
from .models import Category, Entry
from .views import CategoryDetailView, EntryCreateView, EntryUpdateView, json_map_entries_by_tags
from thecaribfos.decorators import ownership_required

urlpatterns = [

    # entry details
    url(r'^entries/(?P<slug>[-\w\d]+)/$',
        DetailView.as_view(
            model = Entry,
            context_object_name = 'entry',
            slug_field = 'slug'
        ),
        name = 'entry_detail'
    ),
    # form add entry
    url(r'^entry/add/$',
        login_required(
            EntryCreateView.as_view()
        ),
        name="form_entry_add",
    ),
    # form update entry
    url(r'^entries/(?P<slug>[-\w\d]+)/update/$',
        login_required(ownership_required(EntryUpdateView.as_view(), model=Entry, owner_field='creation_user')
        ),
        name="form_entry_update",
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

    # index
    url(r'^map/$',
        TemplateView.as_view(
            template_name = 'thedirectory/map/page_map.html'
        ),
        #~ CreateView.as_view(
            #~ form_class=EntryForm,
            #~ template_name='thedirectory/map/page_map.html',
            #~ success_url=reverse_lazy('success')
        #~ ),
        name = 'map'
    ),
    # (leaflet POI js)
    url(r'^map.js$',
        ListView.as_view(model = Entry,
                         template_name = 'thedirectory/map/map.js'
        ),
        name="map_js"
    ),
    url(r'^map/tag/(?P<tag>[-_A-Za-z0-9]+)/entries.json$',
        json_map_entries_by_tags,
        name = 'json_map_entries_by_tags'
    ),


    #~ (r'^tags/$', 'apps.thedirectory.views.tags'),
    #~ (r'^tag/(?P[-_A-Za-z0-9]+)/$','apps.thedirectory.views.with_tag'),
    #~ (r'^tag/(?P[-_A-Za-z0-9]+)/page/(?Pd+)/$', 'apps.thedirectory.views.with_tag' ),
]


