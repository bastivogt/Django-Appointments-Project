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
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        #self.fields["tags"].queryset = Tag.objects.filter(user=user)


    class Meta:
        model = Appointment
        fields = "__all__"
        exclude = [
            "user"
        ]


        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": forms.CheckboxSelectMultiple()
            # "tags": forms.SelectMultiple(attrs={"class": "form-select multiple"})
        }