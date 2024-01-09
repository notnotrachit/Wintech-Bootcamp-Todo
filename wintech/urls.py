"""
URL configuration for wintech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import home, add_task, mark_complete, edit_task, completed_task, mark_incomplete, delete_task
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('add/', add_task, name='add_task'),
    path('complete/<int:task_id>', mark_complete, name='mark_complete'),
    path('incomplete/<int:task_id>', mark_incomplete, name='mark_incomplete'),
    path('edit/<int:task_id>', edit_task, name='edit_task'),
    path('delete/<int:task_id>', delete_task, name='delete_task'),
    path('completed/', completed_task, name='completed_task')
]
