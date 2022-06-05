from django import forms
from errands import models


class ListForm(forms.ModelForm):
    class Meta:
        model = models.List
        fields = ['name']
