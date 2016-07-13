from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.models import *
from apps.forms import *

# To-do list, included query search
class MainPage(LoginRequiredMixin, ListView):
    model = Todo
    def get_queryset(self):
        if self.request.method == 'GET':
            string = self.request.GET.get('q','')
            if string is not None:
                return Todo.objects.filter(user__pk=self.request.user.pk, content__icontains=string).order_by('status')

# Create to-do view
class Create(LoginRequiredMixin, CreateView):
    model = Todo
    success_url = '/'
    form_class = CreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Edit to-do view
class Change(LoginRequiredMixin, UpdateView):
    model = Todo
    success_url = '/'
    form_class = CreateForm

# Delete view for single to-do
class Delete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/'

# Delete view for multiple to-dos
def MDelete(request):
    if request.method == 'GET' or request.method == 'POST':
        item_list = request.GET.getlist('item')
        object_list = []
        for item in item_list:
            object = Todo.objects.get(pk=item)
            object_list.append(object)
        if request.method == 'POST':
            for object in object_list:
                object.delete()
            return redirect('/')
    return render(request, 'apps/todo_confirm_delete_m.html', context={'object_list': object_list})

# Finish to-do
def Finish(request, pk):
    try:
        todo = get_object_or_404(Todo, pk=pk)
    except Todo.DoesNotExist:
        pass
    else:
        todo.status = 'c'
        todo.save()
    return redirect('/')