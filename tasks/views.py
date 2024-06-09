# tasks/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Dashboard view
@login_required
def dashboard(request):
    """Renders the dashboard page."""
    return render(request, 'tasks/dashboard.html')

# Task list view
@login_required
def task_list(request):
    """Renders the task list for the logged-in user."""
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Task detail view
@login_required
def task_detail(request, id):
    """Renders the task detail page for a specific task."""
    task = get_object_or_404(Task, id=id, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

# Task creation view
@login_required
def task_create(request):
    """Handles the creation of a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Task edit view
@login_required
def task_edit(request, id):
    """Handles the editing of an existing task."""
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Task delete view
@login_required
def task_delete(request, id):
    """Handles the deletion of a task."""
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
