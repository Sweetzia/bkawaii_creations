from django import template
# custom template tags and filters, learned from the Boutique Ado project.
# https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity