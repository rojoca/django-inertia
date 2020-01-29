import json
from django import template

register = template.Library()

@register.simple_tag
def inertia_target(data, element_id="app"):
    return '<div id="{element_id}" data-page="{data}"></div>'.format(
        element_id=element_id,
        data=json.dumps(data)
    )
