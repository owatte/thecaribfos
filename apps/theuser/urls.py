from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy

from .views import UserDetailView

urlpatterns = [
    # user public details
    url(r'^(?P<slug>[-\w]+)/$', UserDetailView.as_view(),
    name = 'user_detail'
    ),
]
