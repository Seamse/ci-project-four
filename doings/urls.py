"""doings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from errands import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add', views.add_list, name='add'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('edit_name/<list_id>', views.edit_name, name='edit_name'),
    path('list_status/<list_id>', views.list_status, name='list_status'),
    path('delete_list/<list_id>', views.delete_list, name='delete_list'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<task_id>', views.delete_task, name='delete_task'),
    path('task_status/<task_id>', views.task_status, name='task_status'),
]
