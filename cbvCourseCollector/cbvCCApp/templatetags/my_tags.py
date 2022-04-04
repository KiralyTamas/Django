from django import template
register=template.Library()

@register.filter(name='myUpper')
def my_upper(value):
    word=""
    for index,letter in enumerate(value):
        if index ==0:
            word+=letter.upper()
        else:
            word+=letter
    return word