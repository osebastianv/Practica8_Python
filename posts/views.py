from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from posts.models import Post


class HomeView(ListView):

    model = Post
    template_name = 'posts/list.html'

    def get_queryset(self):
        result = super().get_queryset().select_related().filter(published=True).order_by('-created_on')[:5]
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WordPlease'
        context['claim'] = 'Una plataforma de Blogs para expresar tus ideas'
        return context

        model = Post


class PostDetailView(DetailView):

    model = Post
    template_name = 'posts/detail.html'

    def get_queryset(self):
        try:
            post = super().get_queryset().select_related().filter(id=self.kwargs.get('pk')).filter(published=True)
        except post.DoesNotExist:
            raise Http404("El post solicitado no existe")

        return post



