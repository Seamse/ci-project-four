from django import forms
from errands import models


class ListForm(forms.ModelForm):
    class Meta:
        model = models.List
        fields = ['name']


class TaskForm(forms.ModelForm):
    list = forms.ModelChoiceField(queryset=models.List.objects.all(), initial=models.List.name)

    class Meta:
        model = models.Task
        fields = ['name', 'list']
