from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from datetime import datetime
from posts.forms import NewPostForm
from posts.models import Post


class HomeView(ListView):

    model = Post
    template_name = 'posts/list.html'
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        result = super().get_queryset().select_related().filter(published=True)\
            .filter(owner__is_active=True).order_by('-published_on')

        #result2 = super().get_queryset().prefetch_related("categories").filter(published=True)\
        #    .filter(owner__is_active=True).order_by('-published_on')

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
            post = super().get_queryset().select_related().filter(id=self.kwargs.get('pk'))\
                    .filter(published=True).filter(owner__is_active=True)

        except post.DoesNotExist:
            raise Http404("El post solicitado no existe")

        return post


@method_decorator(login_required, name='dispatch')
class NewPostView (CreateView):
    form_class = NewPostForm
    template_name = 'posts/new-post.html'
    success_message = 'New new user profile has been created'

    def form_valid(self, form):
        #c = {'form': form, }
        post = form.save(commit=False)
        post.owner = self.request.user
        username = post.owner.username

        categories = form.cleaned_data['categories']

        published = form.cleaned_data['published']
        if published == True:
            post.published_on = datetime.now()
        else:
            post.published_on = None
        post.save()

        for category in categories:
            post.categories.add(category)

        url = self.request.GET.get('next', 'user-post-list')
        return redirect(url, username=username)
