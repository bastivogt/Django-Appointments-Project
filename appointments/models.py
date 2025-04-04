from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime
from zoneinfo import ZoneInfo

from django.contrib import admin



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
    date = models.DateTimeField(default=datetime.now, verbose_name=_("Datetime"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"), related_name="appointments")
    
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return f"{self.title}({self.date})"
    

    @admin.display(description="Tags List")
    def tags_str(self):
        all_tags = self.tags.filter(user=self.user)
        all_tags_list = [item.title for item in all_tags]
        return ", ".join(all_tags_list)
    

        
    @admin.display(description="Expired")
    def is_expired(self):
        utc = ZoneInfo("UTC")
        current_date_time = datetime.now(tz=utc)
        return self.date < current_date_time

    @classmethod
    def has_expired(cls, user):
        print("has_expired")
        all = cls.objects.filter(user=user)
        count = 0
        for app in all:
            if app.is_expired():
                
                count += 1
        if count > 0: 
            return True
        return False


    class Meta:
        verbose_name = _("Appointment")
        ordering = [
            "-date",
        ]
