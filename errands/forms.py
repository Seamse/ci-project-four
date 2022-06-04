from django import forms
from errands import models


class NewListForm(forms.ModelForm):
    class Meta:
        model = models.List
        fields = ['name', 'done']
