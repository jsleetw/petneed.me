# encoding: utf-8
from django import template
register = template.Library()

@register.filter
def index_layout_utils(value):
    #if(value.find("收")>-1):
    #print(value.find("收"))
    return value[:8]+"\r\n"+value[8:]

