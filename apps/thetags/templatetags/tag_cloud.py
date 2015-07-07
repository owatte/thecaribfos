from django import template
from django.db.models import get_model
from apps.thedirectory.models import Entry

register = template.Library()


@register.assignment_tag
def tag_cloud_for_model(model_class):
    object_class = get_model(*model_class.split('.'))
    if object_class is None:
        return []
    return object_class.tags.most_common()
