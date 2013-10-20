# encoding: utf-8
from django import template
register = template.Library()

@register.filter
def index_layout_utils(value):
    q = value.split()
    if(len(q)>1):
        results = q[0]+"\r\n"+q[1]
    else:
        results = q[0]+"\r\n"
    return results

