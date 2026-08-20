from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    })


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        Task.objects.create(
            user=request.user,
            title=title,
            description=description
        )

        return redirect('task_list')

    return render(request, 'tasks/add_task.html')


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('task_list')


@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()

        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {'task': task})