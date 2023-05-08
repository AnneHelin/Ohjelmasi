from django.forms import ModelForm, DateInput
from kalenteri.models import Tapahtuma, Tapahtumakalenteri
from django import forms


class Tapahtuma(ModelForm):
    class Meta:
        model = Tapahtuma
        fields = ["title", "description", "start_time", "end_time"]

        # local date and time
        widgets = {
            "title": forms.TextInput(
            attrs={"class": "form-Control",}
            ),
            "desciption": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "give a description",
                }
            ),
            "srart_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time" : DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),    
        }
        exclude  = ["user"]
        def __init__(self, *args, **kwargs):
            super(Tapahtuma, self).__init__(*args, **kwargs)
            # input formats parses HTML5 datetime-local information into a datetime field
            self.fields["start_time"].input_formats = ["%Y-%m-%dT%H:%M",]
            self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class AddMemberform(forms.ModelForm):
        class Meta:
             model = Tapahtumakalenteri
             fields = ["user"]
            

        