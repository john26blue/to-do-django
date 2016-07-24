from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.forms import UserForm

def Register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        User.objects.create_user(username, email, password).save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        next = ''
        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.GET:
                    next = request.GET['next']
                if next == '' or next == None:
                    next = '/'
                return redirect(next)
            else:
                return redirect('/')
        else:
            return redirect('/')

def Logout(request):
    logout(request)
    return redirect(reverse('login'))

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)