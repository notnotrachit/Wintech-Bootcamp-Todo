from django.shortcuts import render
from django.http import HttpResponse
import datetime
from home.models import Task
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    current_date = datetime.datetime.now()
    print(request.user)
    # print(all_students)
    tasks_by_user = Task.objects.filter(created_by=request.user).filter(completed=False)
    return render(
        request,
        'home.html', 
        {
            'current_date': current_date,
            'tasks': tasks_by_user
        }
    )

@login_required
def add_task(request):
    if request.method=="GET":
        return render(request, 'add.html')
    elif request.method=="POST":
        task_name = request.POST['task_name']
        task_description = request.POST['task_description']
        task = Task(title=task_name, description=task_description, created_by=request.user)
        task.save()
        return redirect('home')

@login_required
def mark_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')

@login_required
def mark_incomplete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = False
    task.save()
    return redirect('completed_task')

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method=="GET":
        return render(
            request,
            'edit.html',
            {
                'task': task
            }
        )
    elif request.method=="POST":
        task_name = request.POST['task_name']
        task_description = request.POST['task_description']
        task.title = task_name
        task.description = task_description
        task.save()
        return redirect('home')

@login_required
def completed_task(request):
    completed_tasks= Task.objects.filter(created_by=request.user).filter(completed=True)
    return render(
        request,
        'completed.html',
        {
            'tasks': completed_tasks
        }
    )

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')