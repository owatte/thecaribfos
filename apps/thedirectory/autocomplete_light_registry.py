import autocomplete_light
from django.utils.translation import ugettext as _


from .models import Entry
from taggit.models import Tag

autocomplete_light.register(Tag,
    search_fields=['name'],
    attrs={
        'placeholder': _('tag, tag 1, tag 2 and so on'),
        'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 4,
        'class': 'modern-style',
    },
)
