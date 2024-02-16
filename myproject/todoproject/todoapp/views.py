from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import TASK
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class TaskListview(ListView):
    model=TASK
    template_name = 'home.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model=TASK
    template_name = 'detail.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model=TASK
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = TASK
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
def add(request):
    task1 = TASK.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=TASK(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{"task1":task1})
def delete(request,taskid):
    task=TASK.objects.get(id=taskid)
    if request.method== "POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=TASK.objects.get(id=id)
    form=TaskForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{"form":form,"task":task})


