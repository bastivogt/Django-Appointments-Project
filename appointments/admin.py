from django.contrib import admin

from .models import Appointment, Tag

class TagAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "id",
        "title",
        "created",
        "updated"
    ]

    list_display_links = [
        "id",
        "title"
    ]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "id",
        "title",
        "time",
        "created",
        "updated"
    ]

    list_display_links = [
        "id", 
        "title"
    ]

admin.site.register(Tag, TagAdmin)
admin.site.register(Appointment, AppointmentAdmin)