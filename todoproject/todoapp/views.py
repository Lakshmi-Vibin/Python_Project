from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import ToDoForm
from todoapp.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# views based on class
class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'to_do_list'


class Taskdetailtview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class Taskupdatetview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})

class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvindex')


# Create your views here.


# Views based on functions
def add(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=task_name, priority=priority, date=date)
        task.save()

    detail = Task.objects.all()
    context = {
        'to_do_list': detail
    }
    return render(request, "index.html", context)


# def delete(request, tid):
#     task = Task.objects.get(id=tid)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('/')
#     return render(request, "delete.html")
#
#
# def update(request, tid):
#     task = Task.objects.get(id=tid)
#     form = ToDoForm(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, 'edit.html', {'form': form, 'task': task})
