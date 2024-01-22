from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def home(request):
    return render(request, './base.html')

def AddTask(request):
    task=forms.DoToForm()
    if request.method=='POST':
        task=forms.DoToForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('showtask')
    return render(request, './add_task.html', {'task':task})

def ShowTask(request):
     task = models.ToDoModel.objects.all()
     return render(request, './show_task.html', {'task':task})
 
def DeteteTask(request,id):
    task=models.ToDoModel.objects.get(pk=id).delete()
    return redirect('showtask')

def EditTask(request,id):
    task = models.ToDoModel.objects.get(pk=id)
    form = forms.DoToForm(instance=task)
    if request.method == 'POST':
        form = forms.DoToForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('showtask')
    return render(request, './add_task.html', {'task':form})

def CompleteTask(request,id):
    task = models.ToDoModel.objects.get(pk=id)
    return render(request, './complete_task.html',{'task':task})