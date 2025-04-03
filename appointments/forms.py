from django import forms
from .models import Tag, Appointment


class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["class"] = "form-control"    
    
    class Meta:
        model = Tag
        fields = "__all__"
        exclude = [
            "user"
        ]






class AppointmentForm(forms.ModelForm):
    pass