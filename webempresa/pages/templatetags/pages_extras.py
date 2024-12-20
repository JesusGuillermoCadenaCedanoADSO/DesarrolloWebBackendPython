from django import template
from pages.models import Page

register = template.Library()

# se utiliza el decorador para convertir la funcion en un tag simple y registrarlo en
# la libreria de templates

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages

