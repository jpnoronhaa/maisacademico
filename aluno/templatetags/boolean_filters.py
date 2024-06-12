from django import template

register = template.Library()

@register.filter(name='bool_to_text')
def bool_to_text(value):
  return "Sim" if value else "Não"
