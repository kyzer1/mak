import imp
from django import template
from django.utils.safestring import mark_safe

register=template.Library()

@register.simple_tag
def split_prop_func(prop:str):
    result=""
    if "/" in prop:
        splited_prop=prop.split("/")
    else:
        splited_prop=prop.split()
    
    for i in splited_prop:
        result += '<a href="">'+f"{i} "+'</a>'
    
    return mark_safe(result)
       

    
