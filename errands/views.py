from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from errands import forms
from .models import List, Task


def home(request):
    if request.user.is_authenticated:
        lists = List.objects.filter(user=request.user)
        context = {
            'lists': lists
        }
    else:
        context = {
            'lists': {}
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
    return redirect(request.META.get('HTTP_REFERER'))


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


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return redirect(request.META.get('HTTP_REFERER'))


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = forms.TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = forms.TaskForm(instance=task)
    context = {
        'form': form
    }
    return render(request, "edit_task.html", context)


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Registration failed. Invalid information.")
    form = forms.RegistrationForm()
    context = {
        'form': form
    }
    return render(request, "register.html", context)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, "login.html", context)


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')
