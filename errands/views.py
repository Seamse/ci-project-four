from django.shortcuts import render, redirect, get_object_or_404
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


def edit(request, list_id):
    list = get_object_or_404(List, id=list_id)
    context = {
        'list': list
    }
    return render(request, 'edit_redirect.html', context)
