from django.shortcuts import render
from .models import List


def home(request):
    lists = List.objects.all()
    context = {
        'lists': lists
    }
    return render(request, 'index.html', context)
