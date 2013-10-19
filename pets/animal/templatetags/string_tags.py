from django import template

register = template.Library()

@register.simple_tag
def cut_string(input_string, num):
    return input_string[0:num]
