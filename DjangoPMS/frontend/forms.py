from django import forms
from django.contrib.gis import forms as geo_forms


class ReserveForm(forms.Form):
    arrival = forms.DateTimeField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "datetime-local"})
    )
    location = forms.CharField(max_length=40, label="Where are you going?")
