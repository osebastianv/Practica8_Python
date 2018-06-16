from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostDetailSerializer, NewPostSerializer


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    permission_classes = [PostPermission]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'intro', 'body']
    ordering_fields = ['title', 'published_on']

    def get_serializer_class(self):
        if self.action == 'create':
            return NewPostSerializer
        elif self.action == 'list':
            return PostListSerializer
        else:
            return PostDetailSerializer

    def get_queryset(self):
        username = self.request.user.username
        is_authenticated = self.request.user.is_authenticated

        if is_authenticated:
            is_superuser = self.request.user.is_superuser

            if is_superuser:
                result = super().get_queryset().select_related().filter().order_by('-published_on')
            else:
                result = super().get_queryset().select_related().filter(owner__username=username) \
                    .order_by('-published_on')
        else:
            result = super().get_queryset().select_related().filter(published=True).filter(owner__is_active=True) \
                .order_by('-published_on')

        return result

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
