from django import template

register = template.Library()

def slug2js(value):
    '''replace - with _'''

    return value.replace('-', '_')

register.filter('slug2js', slug2js)
