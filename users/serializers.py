from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from django.contrib.auth.models import User
from rest_framework.reverse import reverse


class UserListSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username']


class NewUserSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailSerializer(ModelSerializer):

    class Meta:

        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']


class UserPostListSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = User
        fields = ['username']

    #def list(self):

    """
    def get_url(self, obj, view_name, request):
        kwargs = {'username': obj.get('username')}
        return reverse(view_name, kwargs=kwargs, request=request)
    """