from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.models import *
from apps.forms import *

# Create your views here.
class MainPage(LoginRequiredMixin, ListView):
    model = Todo
    def get_queryset(self):
        if self.request.method == 'GET':
            string = self.request.GET.get('q','')
            if string is not None:
                return Todo.objects.filter(user__pk=self.request.user.pk, content__icontains=string).order_by('status')

class Create(LoginRequiredMixin, CreateView):
    model = Todo
    success_url = '/'
    form_class = CreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Change(LoginRequiredMixin, UpdateView):
    model = Todo
    success_url = '/'
    form_class = CreateForm

class Delete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/'

def Finish(request, pk):
    try:
        todo = get_object_or_404(Todo, pk=pk)
    except Todo.DoesNotExist:
        pass
    else:
        todo.status = 'c'
        todo.save()
    return redirect('/')