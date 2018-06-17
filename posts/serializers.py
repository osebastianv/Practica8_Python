from rest_framework.serializers import ModelSerializer
from django.template.defaultfilters import filesizeformat
from django.conf import settings

from datetime import datetime
from posts.models import Post


class PostListSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'owner', 'title', 'intro', 'url', 'published_on']

    def retrieve(self, validated_data):
        post = super().create(validated_data)
        return post


class NewPostSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['title', 'intro', 'body', 'url', 'categories']

    def validate_url(self, value):
        url = value
        if url is not None:
            content_type = url.content_type.split('/')[0]
            if content_type not in settings.CONTENT_TYPES:
                raise ModelSerializer.ValidationError('El archivo no es válido, solo permite imágenes o videos')
            if url.size > int(settings.MAX_UPLOAD_SIZE):
                raise ModelSerializer.ValidationError('Por favor, conserve el tamaño del archivo por debajo %(value)s. '
                                      'Tamaño actual: %(value2)s',
                                      params={'value': filesizeformat(settings.MAX_UPLOAD_SIZE),
                                              'value2': filesizeformat(url.size)})
        return value

    def create(self, validated_data):
        post = super().create(validated_data)
        post.published = True
        post.published_on = datetime.now()

        content_type_exits = hasattr(validated_data["url"], 'content_type')

        if post.url != "" and content_type_exits:
            post.content_type = validated_data["url"].content_type
        post.save()
        return post


class PostDetailSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'title', 'intro', 'body', 'url', 'published', 'published_on', 'categories']
