from django.contrib import admin

from .forms import EntryForm
from apps.thedirectory.models import Category, Entry

#~ class EntryAdmin(admin.ModelAdmin):
    #~ form = EntryForm
    #list_display = ['tags']

admin.site.register(Category)
admin.site.register(Entry)
