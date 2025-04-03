from django.shortcuts import render
from django.conf import settings
from django.http import Http404
import os


def index(request):
    return render(request, "pages/index.html", {
        "title": "pages#views#index"
    })

def page(request, name):
    file_name = f"{name}.html"
    file_path = os.path.join(settings.BASE_DIR, "pages", "templates", "pages", file_name)
    print(file_path)
    print(os.path.isfile(file_path))

    if not os.path.isfile(file_path):
        raise Http404()

    return render(request, f"pages/{file_name}", {
        "title": name.title()
    })
