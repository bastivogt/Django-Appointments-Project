from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime

from django.contrib.auth import get_user_model
User = get_user_model()

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = [
            "-updated"
        ]
        verbose_name = _("Tag")


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    time = models.DateTimeField(default=datetime.now, verbose_name=_("Datetime"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"), related_name="appointments")
    
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return f"{self.title}({self.time})"

    class Meta:
        verbose_name = _("Appointment")
        ordering = [
            "-time"
        ]
