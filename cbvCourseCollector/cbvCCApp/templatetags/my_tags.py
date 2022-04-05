from django import template
register=template.Library()

@register.filter(name='firstLetter')
def my_upper(value):
    word=""
    for index,letter in enumerate(value):
        if index ==0:
            word+=letter.upper()
        else:
            word+=letter
    return word

@register.filter(name="everyFirstLetter")
def proba(value):
    space=" "
    words=""
    for index,letter in enumerate(value):
        if index ==0 or space == words[-1]:
            words+=letter.upper()
        else:
            words+=letter
    return words