from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(max_length=200)
    #completed = forms.BooleanField(required=False)