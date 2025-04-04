from django.urls import path

from .views import appointments
from .views import tags

app_name = "appointments"
urlpatterns = [
    # appointments
    path("appointments/", appointments.index, name="index"),
    path("appointments/<int:pk>/", appointments.show, name="show"),
    path("appointments/new/", appointments.new, name="new"),
    path("appointments/<int:pk>/update/", appointments.update, name="update"),
    path("appointments/delete/expired/", appointments.delete_expired, name="delete_expired"),
    path("appointments/<int:pk>/delete/", appointments.delete, name="delete"),

    #tags
    path("tags/", tags.index, name="tags_index"),
    path("tags/new/", tags.new, name="tags_new"),
    path("tags/<int:pk>/", tags.show, name="tags_show"),
    path("tags/<int:pk>/update/", tags.update, name="tags_update"),
    path("tags/<int:pk>/delete/", tags.delete, name="tags_delete"),
    
]
