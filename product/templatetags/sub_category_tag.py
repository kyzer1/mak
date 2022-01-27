from django import template

register = template.Library()

@register.simple_tag
def get_sub_cat(product_category):
    sub_category = product_category.child_cat.all()
    return sub_category