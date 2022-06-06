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
        form = forms.ListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = forms.ListForm()
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


def edit_name(request, list_id):
    list = get_object_or_404(List, id=list_id)
    if request.method == "POST":
        form = forms.ListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = forms.ListForm(instance=list)
    context = {
        'form': form
    }
    return render(request, "edit_name.html", context)


def list_status(request, list_id):
    list = get_object_or_404(List, id=list_id)
    list.done = not list.done
    list.save()
    return redirect('home')


def delete_list(request, list_id):
    list = get_object_or_404(List, id=list_id)
    list.delete()
    return redirect('home')


def add_task(request):
    if request.method == "POST":
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = forms.TaskForm()
    context = {
        'form': form
    }
    return render(request, "add_task.html", context)
