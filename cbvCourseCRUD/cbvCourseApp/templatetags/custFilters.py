from django import template

register = template.Library()

@register.filter(name="myLower")
def custLower(value):
    result = value[:3].lower()
    return result
# def custLower(value):
#     result = value[:3].lower()
#     return result
#
#
# register.filter("myLower", custLower)


@register.filter(name="myAppend")
def custAppend(value,arg):
    result = str(arg)+value
    return result