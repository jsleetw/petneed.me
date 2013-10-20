#-*- coding: UTF-8 -*-
from django.forms import ModelForm
from animal.models import LostAnimal


class LostAnimalForm(ModelForm):
    class Meta:
        model = LostAnimal
        exclude = ['found',]
