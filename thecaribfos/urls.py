from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.flatpages import views
from django.views.generic import ListView, TemplateView
from django.views.i18n import javascript_catalog

import autocomplete_light.shortcuts as al
from apps.thecalendar.models import Event
from apps.thehomepage.views import HomePageDetailView

js_info_dict = {
    'packages': ('thecaribfos.apps.thedirectory',),
}

urlpatterns = [
    # main index
    url(r'^$',
        #~ ListView.as_view(
            #~ model = Event,
            #~ template_name = 'home.html'
        #~ ),
        HomePageDetailView.as_view(),
        name = 'home'
    ),
    url(r'^calendar/', include("apps.thecalendar.urls", namespace="thecalendar")),
    url(r'^directory/', include("apps.thedirectory.urls", namespace="thedirectory")),

    url(r'^caribbean/', include("apps.thecarib.urls", namespace="thecarib")),
    url(r'^contact/', include('apps.thecontactform.urls', namespace="thecontactform")),

    url(r'^account/', include("account.urls")),
    url(r'^account/$', login_required(TemplateView.as_view(
            template_name = 'account/profile.html')
        ),
        name = 'account_profile'
    ),
    url(r"^account/social/", include("social.apps.django_app.urls", namespace="social")),

    url(r'^admin/', include(admin.site.urls)),
    # form submission success
    url(r'^contribute/success/$',
        TemplateView.as_view(template_name="include/success.html"),
        name='success'
    ),
    #~ url(r'^markdown/', include('django_bootstrap_markdown.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
    #~ url(r'^(?P<url>.*/)$', views.flatpage),
]


