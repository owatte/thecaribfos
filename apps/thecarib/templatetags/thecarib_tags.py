from django import template

from apps.thecarib.models import Country

register = template.Library()

@register.inclusion_tag('thecarib/tags/filter_country.html', takes_context=True)
def show_filter_country(context):
    countries = Country.objects.all()
    try:
        country_name = countries.get(iso = context['request'].GET.get('country'))
    except Country.DoesNotExist:
        country_name = None

    return {'countries': countries,
            'request': context['request'],
            'country_name': country_name
    }
