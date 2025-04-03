from django.urls import path

from .views import appointments
from .views import tags

app_name = "appointments"
urlpatterns = [
    # appointments
    path("appointments/", appointments.index, name="index"),

    #tags
    path("tags/", tags.index, name="tags_index"),
    path("tags/new/", tags.new, name="tags_new"),
    path("tags/<int:pk>/", tags.show, name="tags_show"),
    path("tags/<int:pk>/update", tags.update, name="tags_update"),
    path("tags/<int:pk>/delete", tags.delete, name="tags_delete"),
    
]
