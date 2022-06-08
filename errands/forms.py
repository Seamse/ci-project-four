from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from errands import models


class ListForm(forms.ModelForm):
    class Meta:
        model = models.List
        fields = ['name']


class TaskForm(forms.ModelForm):
    list = forms.ModelChoiceField(queryset=models.List.objects.all())

    class Meta:
        model = models.Task
        fields = ['name', 'list']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
