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
        "date",
        "tags_str",
        "is_expired",
        "created",
        "updated"
    ]

    list_display_links = [
        "id", 
        "title"
    ]

    list_filter = [
        "date",
 
    ]

    readonly_fields = [
        "is_expired"
    ]




admin.site.register(Tag, TagAdmin)
admin.site.register(Appointment, AppointmentAdmin)