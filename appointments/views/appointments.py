from django.shortcuts import render




def index(request):
    return render(request, "appointments/index.html", {
        "title": "appointments#views#appointments#index"
    })