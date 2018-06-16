from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views import View

from posts.models import Post
from django.contrib.auth.models import User
from users.forms import LoginForm, SignupForm


class UsersView(ListView):

    model = User
    template_name = 'users/list.html'
    context_object_name = "user_list"
    paginate_by = 5

    def get_queryset(self):
        result = super().get_queryset().filter(is_active=True).order_by('date_joined')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Blogs de usuario'
        return context


class UserPostView(ListView):

    model = Post
    template_name = 'posts/list.html'
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        username = self.kwargs.get("username")

        is_authenticated = self.request.user.is_authenticated

        if is_authenticated:
            result = super().get_queryset().select_related().filter(owner__username=username)\
                    .order_by('-published_on')
        else:
            result = super().get_queryset().select_related().filter(owner__username=username)\
                    .filter(published=True).filter(owner__is_active=True)\
                    .order_by('-published_on')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get("username")
        context['title'] = 'Listado de últimos posts ' + username
        return context

class LoginView(View):

    def get(self, request):
        """
        Muestra el formulario de login
        :param request: objeto HttpRequest
        :return: objeto HttpResponse con el formulario renderizado
        """
        form = LoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Procesa el login de un usuario
        :param request: objeto HttpRequest
        :return: objeto HttpResponse con el formulario renderizado
        """
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # comprobamos si las credenciales son correctas
            # Si el usuario está inactivo tampoco pasa
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario o contraseña incorrecto')
            else:
                # iniciamos la sesión del usuario (hacemos login del usuario)
                django_login(request, user)
                url = request.GET.get('next', 'user-post-list')
                return redirect(url, username=username)

        context = {'form': form}
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        """
        Hace logout de un usuario y le redirige al login
        :param request: objeto HttpRequest
        :return: objeto HttpResponse de redirección al login
        """
        django_logout(request)
        return redirect('login')


class SignupView (CreateView):
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_message = 'New new user profile has been created'

    def form_valid(self, form):
        c = {'form': form, }
        user = form.save(commit=False)
        # Cleaned(normalized) data
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        if password != repeat_password:
            messages.error(self.request, "Las contraseñas no coinciden", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user.set_password(password)
        user.save()

        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
        new_user = authenticate(username=username, password=password)
        django_login(self.request, new_user)

        url = self.request.GET.get('next', 'user-post-list')
        return redirect(url, username=username)

