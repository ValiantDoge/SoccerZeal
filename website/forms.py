from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"name"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"email"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id":"subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "id":"message"}))