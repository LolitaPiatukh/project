from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm


def index(request):
    task = Task.objects.order_by('-id')
    return render(request,'taskmanager2/index.html',{'title':'Главная страница сайта','tasks': task})

def about(request):
    return render(request,'taskmanager2/about.html')

def create(request):
    error = " "
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = ' Форма была неверной'

    form =TaskForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request,'taskmanager2/create.html',context)


# Create your views here.
