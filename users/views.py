from django.contrib.auth.models import User
from django.views.generic import ListView

from posts.models import Post


class UsersView(ListView):

    model = User
    template_name = 'users/list.html'
    context_object_name = "user_list"
    paginate_by = 3

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
    paginate_by = 3

    def get_queryset(self):
        username = self.kwargs.get("username")
        result = super().get_queryset().select_related().filter(owner__username=username).filter(published=True).order_by('-created_on')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get("username")
        context['title'] = 'Listado de últimos posts ' + username
        return context
