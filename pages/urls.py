from django.urls import path


from . import views

app_name = "pages"
urlpatterns = [
    path("<str:name>/", views.page, name="page"),
    path("", views.index, name="index")
]
