from django import template

register = template.Library()

@register.filter
def split(value, separator=','):
    """Divide uma string em lista."""
    if value:
        return [v.strip() for v in value.split(separator)]
    return []
