from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})


@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('task_list')

    return render(request, 'task_form.html', {'form': form})


@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)

    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')

    return render(request, 'task_form.html', {'form': form})


@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')

@login_required
def task_list(request):

    search = request.GET.get('search')

    tasks = Task.objects.filter(user=request.user)

    if search:
        tasks = tasks.filter(title__icontains=search)

    paginator = Paginator(tasks, 5)

    page = request.GET.get('page')

    tasks = paginator.get_page(page)

    return render(request,'task_list.html',{'tasks':tasks})