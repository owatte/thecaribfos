from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from django.views.generic import TemplateView
from apps.thedirectory.models import Entry
from apps.thecalendar.models import Event
from django.contrib.auth.models import User

class UserDetailView(TemplateView):
    template_name = 'theuser/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView,self).get_context_data(**kwargs)

        #~ context['user'] = User.objects.get(username__exact=self.request['username'])

        context['user'] = User.objects.get(username__exact='admin')
        context['entries'] = Entry.objects.filter(creation_user__username__exact='admin')
        context['events'] = Event.objects.filter(creation_user__username__exact='admin')

        return context
