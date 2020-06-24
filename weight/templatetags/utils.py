from django import template


register = template.Library()

@register.filter(name="bmicalculation")
def bmicalculation(value, args):
    bmi = value / (args / 100)**2
    return bmi