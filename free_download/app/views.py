from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from app.models import Programs
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView
from .forms import CommentForm


class ProgramsHome(ListView):
    paginate_by = 12
    model = Programs
    template_name = 'index.html'
    context_object_name = 'programs'


class ProgramPost(FormMixin, DetailView):
    model = Programs
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('show_post', kwargs={'post_slug': self.get_object().slug})


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ProgramsCategory(ListView):
    model = Programs
    template_name = 'index.html'
    context_object_name = 'programs'

    def get_queryset(self):
        return Programs.objects.filter(cat__slug=self.kwargs['cat_slug'])




def registration_view(request):
    context = {}
    form = RegistrationForm()
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=pwd)

            if user is not None:
                login(request, user)
                return redirect("home")

    context = {'form': form}
    return render(request, 'register.html', context)



def logoutUser(requeset):
    logout(requeset)
    return redirect('login')


def login_view(request):

    context = {}
    form = RegistrationForm
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {'form': form}
    return render(request, "login.html", context)
