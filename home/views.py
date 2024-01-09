from django.shortcuts import render
from django.http import HttpResponse
import datetime
from home.models import Task

# Create your views here.
def home(request):
    current_date = datetime.datetime.now()
    print(request.user)
    # print(all_students)
    tasks_by_user = Task.objects.filter(created_by=request.user)
    return render(
        request,
        'home.html', 
        {
            'current_date': current_date,
            'tasks': tasks_by_user
        }
    )