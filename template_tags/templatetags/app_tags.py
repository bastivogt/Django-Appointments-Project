from django import template
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string





register = template.Library()

@register.simple_tag
def active_site(path, name):
    # print(path)
    path_splitted = path.split("/")
    # print(path_splitted)
    path_compare = path_splitted[2]
    if name in path_compare:
        return "active"
 
    


# tags for db content
@register.simple_tag
def greeting(name="John"):
    return f"Hello, {name}!"