from django import forms


class DriverForm(forms.ModelForm):
    username = forms.CharField(label="Your name", max_length=150)
    password = forms.CharField(label="Your password", max_length=128)
    email = forms.EmailField(label="Your Email")
