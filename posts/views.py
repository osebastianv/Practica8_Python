from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from posts.models import Post


class HomeView(ListView):

    model = Post
    template_name = 'posts/list.html'
    context_object_name = "post_list"
    paginate_by = 3

    def get_queryset(self):
        result = super().get_queryset().select_related().filter(published=True).order_by('-created_on')
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de últimos posts'
        return context


class PostDetailView(DetailView):

    model = Post
    template_name = 'posts/detail.html'

    def get_queryset(self):
        try:
            post = super().get_queryset().select_related().filter(id=self.kwargs.get('pk')).filter(published=True)
        except post.DoesNotExist:
            raise Http404("El post solicitado no existe")

        return post



