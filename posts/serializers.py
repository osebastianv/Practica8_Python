from rest_framework.serializers import ModelSerializer

from datetime import datetime
from posts.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'owner', 'title', 'intro', 'url', 'published_on']


class NewPostSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['title', 'intro', 'body', 'url', 'categories']

    def create(self, validated_data):
        post = super().create(validated_data)
        post.published = True
        post.published_on = datetime.now()
        post.save()
        return post


class PostDetailSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'title', 'intro', 'body', 'url', 'published', 'published_on', 'categories']
