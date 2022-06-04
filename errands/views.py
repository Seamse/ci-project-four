from django.shortcuts import render, redirect
from errands import forms
from .models import List


def home(request):
    lists = List.objects.all()
    context = {
        'lists': lists
    }
    return render(request, 'index.html', context)


def add_list(request):
    if request.method == "POST":
        form = forms.NewListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = forms.NewListForm()
    context = {
        'form': form
    }
    return render(request, "add_list.html", context)
