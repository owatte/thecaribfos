from django.conf.urls import url
#~ from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
#~
#~
#~ from apps.thedirectory.models import Entry
#~ from apps.thecalendar.models import Event
#~
from .models import Country

from .views import CountryDetail

urlpatterns = [

    url(r'^$',
        ListView.as_view(
            model = Country,
            context_object_name = 'countries'
        ),
        name = 'country_list'
    ),

    url(r'^(?P<slug>[-\w\d]+)/$',
        CountryDetail.as_view(),
        #~ DetailView.as_view(
            #~ model = Country,
            #~ context_object_name = 'country',
            #~ slug_field = 'iso'
        #~ ),
        name = 'country_detail'
    ),

]


