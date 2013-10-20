#-*- coding: UTF-8 -*-
from django import forms

class LostAnimalForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
)
